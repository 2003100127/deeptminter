__author__ = "Jianfeng Sun"
__version__ = "v1.0"
__copyright__ = "Copyright 2025"
__license__ = "GPL v3.0"
__email__ = "jianfeng.sunmt@gmail.com"
__maintainer__ = "Jianfeng Sun"

import numpy as np
import pandas as pd
from deeptminter.util.Reader import Reader as pfreader


class Cumulative:
    
    def __init__(self, sequence, window_size, window_aa_ids):
        self.window_size = window_size
        self.window_aa_ids = window_aa_ids
        self.num_aas = len(self.window_aa_ids)
        self.sequence = sequence
        self.len_seq = len(self.sequence)
        self.pfreader = pfreader()

    def tfers(self, value):
        return 1 / (1 + np.exp(-value))

    def assign(self, list_2d, L, prot_name, file_chain, fc_activate=False, cp_activate=False, plmc_activate=False, gdca_activate=False, mi_activate=False, fc_path=None, cp_path=None, plmc_path=None, gdca_path=None, mi_path=None):
        list_2d_ = list_2d
        local_pair_ids = self.window_aa_ids
        if fc_path is not None:
            fc_sum = self.freecontact(
                fc_path=fc_path,
                file_name=prot_name,
                file_chain=file_chain,
                sort_=3,
                is_sort=True
            )['score'].sum()
            fc_ave = fc_sum / self.len_seq
            fc_dict = self.freecontact(
                fc_path=fc_path,
                file_name=prot_name,
                file_chain=file_chain,
                sort_=7,
                len_seq=self.len_seq,
                L=L
            )
            for i, aa_win_ids in enumerate(local_pair_ids):
                for j in aa_win_ids:
                    if j is None:
                        list_2d_[i].append(0)
                    else:
                        if fc_activate:
                            list_2d_[i].append(self.tfers(fc_dict[j] / fc_ave))
                        else:
                            list_2d_[i].append(fc_dict[j] / fc_ave)
        if cp_path is not None:
            cp_sum = self.ccmpred(
                cp_path=cp_path,
                file_name=prot_name,
                file_chain=file_chain,
                sort_=3,
                is_sort=True
            )['score'].sum()
            cp_ave = cp_sum / self.len_seq
            cp_dict = self.ccmpred(
                cp_path=cp_path,
                file_name=prot_name,
                file_chain=file_chain,
                sort_=7,
                len_seq=self.len_seq,
                L=L
            )
            for i, aa_win_ids in enumerate(local_pair_ids):
                for j in aa_win_ids:
                    if j is None:
                        list_2d_[i].append(0)
                    else:
                        if cp_activate:
                            list_2d_[i].append(self.tfers(cp_dict[j] / cp_ave))
                        else:
                            list_2d_[i].append(cp_dict[j] / cp_ave)
        if plmc_path is not None:
            plmc_sum = self.plmc(
                plmc_path=plmc_path,
                file_name=prot_name,
                file_chain=file_chain,
                sort_=3,
                is_sort=True
            )['score'].sum()
            plmc_ave = plmc_sum / self.len_seq
            plmc_dict = self.plmc(
                plmc_path=plmc_path,
                file_name=prot_name,
                file_chain=file_chain,
                sort_=7,
                len_seq=self.len_seq,
                L=L
            )
            for i, aa_win_ids in enumerate(local_pair_ids):
                for j in aa_win_ids:
                    if j is None:
                        list_2d_[i].append(0)
                    else:
                        if plmc_activate:
                            list_2d_[i].append(self.tfers(plmc_dict[j] / plmc_ave))
                        else:
                            list_2d_[i].append(plmc_dict[j] / plmc_ave)
        if gdca_path is not None:
            gdca_sum = self.gdca(
                gdca_path=gdca_path,
                file_name=prot_name,
                file_chain=file_chain,
                sort_=3,
                is_sort=True
            )['score'].sum()
            gdca_ave = gdca_sum / self.len_seq
            gdca_dict = self.gdca(
                gdca_path=gdca_path,
                file_name=prot_name,
                file_chain=file_chain,
                sort_=7,
                len_seq=self.len_seq,
                L=L
            )
            for i, aa_win_ids in enumerate(local_pair_ids):
                for j in aa_win_ids:
                    if j is None:
                        list_2d_[i].append(0)
                    else:
                        if gdca_activate:
                            list_2d_[i].append(self.tfers(gdca_dict[j] / gdca_ave))
                        else:
                            list_2d_[i].append(gdca_dict[j] / gdca_ave)
        if mi_path is not None:
            mi_sum = self.mi(
                mi_path=mi_path,
                file_name=prot_name,
                file_chain=file_chain,
                sort_=3,
                is_sort=True
            )['score'].sum()
            mi_ave = mi_sum / self.len_seq
            mi_dict = self.mi(
                mi_path=mi_path,
                file_name=prot_name,
                file_chain=file_chain,
                sort_=7,
                len_seq=self.len_seq,
                L=L
            )
            for i, aa_win_ids in enumerate(local_pair_ids):
                for j in aa_win_ids:
                    if j is None:
                        list_2d_[i].append(0)
                    else:
                        if mi_activate:
                            list_2d_[i].append(self.tfers(mi_dict[j] / mi_ave))
                        else:
                            list_2d_[i].append(mi_dict[j] / mi_ave)
        return list_2d_

    def todict(self, recombine):
        arr_2d = recombine.values.tolist()
        dicts = self.letsrt(arr_2d)
        return dicts

    def letsrt(self, arr_2d):
        result = {}
        len_arr = len(arr_2d[0])
        if len_arr == 3:
            for item in arr_2d:
                result.setdefault(item[0], {}).update({item[1]: item[2]})
        else:
            for item in arr_2d:
                result.setdefault(item[0], {}).update({item[1]: item[2:]})
        return result

    def sort_3(self, recombine, is_sort=False, is_uniform=False, uniform_df=None, indicator=0):
        juct = recombine
        if is_uniform:
            predict_dict = self.todict(juct)
            uniform_df[2] = indicator
            uniform_list = uniform_df.values.tolist()
            uniform_shape = len(uniform_list)
            for i in range(uniform_shape):
                id_1 = uniform_list[i][0]
                id_2 = uniform_list[i][1]
                try:
                    uniform_list[i][2] = predict_dict[id_1][id_2]
                except KeyError:
                    continue
            juct = pd.DataFrame(uniform_list)
            juct.columns = [
                'contact_id_1',
                'contact_id_2',
                'score'
            ]
        juct = self.extract(
            tq=juct,
            first='contact_id_1',
            second='contact_id_2',
            target='score',
            seq_sep_inferior=None,
            seq_sep_superior=None,
            is_sort=is_sort
        )
        return juct

    def extract(self, tq, first, second, target, seq_sep_inferior, seq_sep_superior, is_sort):
        if seq_sep_inferior is not None and seq_sep_superior is None:
            query = (tq[second] - tq[first] > seq_sep_inferior)
        elif seq_sep_inferior is None and seq_sep_superior is not None:
            query = (tq[second] - tq[first] < seq_sep_superior)
        elif seq_sep_inferior is not None and seq_sep_superior is not None:
            ss_inf = tq[second] - tq[first] > seq_sep_inferior
            ss_sup = tq[second] - tq[first] < seq_sep_superior
            query = (ss_inf & ss_sup)
        else:
            query = (0 < tq[second] - tq[first])
        tq = tq.loc[query].sort_values(
            by=[first, second],
            ascending=True
        )
        if is_sort:
            tq = tq.loc[query].sort_values([target], ascending=False)
        else:
            tq = tq.loc[query]
        tq = tq.reset_index(inplace=False, drop=True)
        return tq

    def sort_6(self, recombine, id, L):
        juct = recombine
        constraint_1 = (juct['contact_id_1'] == id)
        query = constraint_1
        juct = juct.loc[query]
        juct = juct.sort_values(
            by=['score'],
            ascending=False
        ).iloc[0: L, :]
        return juct

    def cumulative(self, recombine, L, len_seq):
        juct = recombine
        cumu_dict = dict()
        for i in range(len_seq):
            recombine_cumu = self.sort_6(juct, id=i + 1, L=L)
            cumu_dict[i + 1] = self.addition(recombine_cumu)
        return cumu_dict

    def addition(self, recombine):
        juct = recombine
        cumu = juct['score'].sum()
        return cumu

    def mi(self, mi_path, file_name, file_chain, sort_=0, is_sort=False, L=50, len_seq=50):
        self.__sort_ = sort_
        results = self.pfreader.generic(
            mi_path + file_name + file_chain + '.evfold',
            df_sep='\s+',
            is_utf8=True
        )
        results.columns = [
            'contact_id_1',
            'aa_1',
            'contact_id_2',
            'aa_2',
            'score',
            'FC_score'
        ]
        recombine = results[[
            'contact_id_1',
            'contact_id_2',
            'score'
        ]]
        if self.__sort_ == 3:
            recombine = self.sort_3(recombine, is_sort=is_sort)
            return recombine
        elif self.__sort_ == 7:
            cumu_dict = self.cumulative(recombine, L=L, len_seq=len_seq)
            return cumu_dict

    def freecontact(self, fc_path, file_name, file_chain, sort_=0, is_sort=False, L=50, len_seq=50):
        self.__sort_ = sort_
        results = self.pfreader.generic(
            fc_path + file_name + file_chain + '.evfold',
            df_sep='\s+',
            is_utf8=True
        )
        results.columns = [
            'contact_id_1',
            'aa_1',
            'contact_id_2',
            'aa_2',
            'MI_score',
            'score'
        ]
        recombine = results[[
            'contact_id_1',
            'contact_id_2',
            'score'
        ]]
        if self.__sort_ == 3:
            recombine = self.sort_3(recombine, is_sort=is_sort)
            return recombine
        elif self.__sort_ == 7:
            cumu_dict = self.cumulative(recombine, L=L, len_seq=len_seq)
            return cumu_dict

    def ccmpred(self, cp_path, file_name, file_chain, sort_=0, is_sort=False, L=50, len_seq=50):
        self.__sort_ = sort_
        file_results = self.pfreader.generic(
            cp_path + file_name + file_chain + '.ccmpred',
            df_sep='\s+',
            is_utf8=True
        )
        results = []
        for i, row in file_results.iterrows():
            for j in range(file_results.shape[1]):
                if i < j:
                    results.append([i + 1, j + 1, row[j]])
        results = pd.DataFrame(results)
        results.columns = [
            'contact_id_1',
            'contact_id_2',
            'score'
        ]
        recombine = results[[
            'contact_id_1',
            'contact_id_2',
            'score'
        ]]
        if self.__sort_ == 3:
            recombine = self.sort_3(recombine, is_sort=is_sort)
            return recombine
        elif self.__sort_ == 7:
            cumu_dict = self.cumulative(recombine, L=L, len_seq=len_seq)
            return cumu_dict

    def gdca(self, gdca_path, file_name, file_chain, sort_=0, is_sort=False, L=50, len_seq=50):
        self.__sort_ = sort_
        results = self.pfreader.generic(
            gdca_path + file_name + file_chain + '.gdca',
            df_sep='\s+',
            is_utf8=True
        )
        results.columns = [
            'contact_id_1',
            'contact_id_2',
            'score'
        ]
        recombine = results[[
            'contact_id_1',
            'contact_id_2',
            'score'
        ]]
        if self.__sort_ == 3:
            recombine = self.sort_3(recombine, is_sort=is_sort)
            return recombine
        elif self.__sort_ == 7:
            cumu_dict = self.cumulative(recombine, L=L, len_seq=len_seq)
            return cumu_dict

    def plmc(self, plmc_path, file_name, file_chain, sort_=0, is_sort=False, L=50, len_seq=50):
        self.__sort_ = sort_
        results = self.pfreader.generic(
            plmc_path + file_name + file_chain + '.plmc',
            df_sep='\s+',
            is_utf8=True
        )
        results.columns = [
            'contact_id_1',
            'aa_1',
            'contact_id_2',
            'aa_2',
            'placeholder',
            'score'
        ]
        recombine = results[[
            'contact_id_1',
            'contact_id_2',
            'score'
        ]]
        if self.__sort_ == 3:
            recombine = self.sort_3(recombine, is_sort=is_sort)
            return recombine
        elif self.__sort_ == 7:
            cumu_dict = self.cumulative(recombine, L=L, len_seq=len_seq)
            return cumu_dict