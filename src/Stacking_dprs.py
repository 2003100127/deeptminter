__author__ = "Jianfeng Sun"
__version__ = "v1.0"
__copyright__ = "Copyright 2020"
__license__ = "GPL v3.0"
__email__ = "jianfeng.sunmt@gmail.com"
__maintainer__ = "Jianfeng Sun"

import numpy as np
import pandas as pd
from sklearn.externals import joblib
from src.Reader_dprs import reader_dprs as pfrreader
from src.SSFasta_dprs import fasta_dprs as sfasta
from src.Kind_dprs import kind_dprs
from src.Length_dprs import length_dprs as plength
from src.Phobius_dprs import phobius_dprs


class stacking_dprs(object):

    def __init__(self, RELEASE=None):
        self.RELEASE = RELEASE
        self.pfrread = pfrreader()
        self.sequence = sfasta().getMerged(self.RELEASE['input_path'] + self.RELEASE['prot_name'] + self.RELEASE['file_chain'] + '.fasta')
        self.usl = plength().toSingle(len(self.sequence))

    def dprs(self, dprs_path, prot_name, file_chain, file_suffix):
        results = self.pfrread.generic(
            dprs_path + prot_name + file_chain + file_suffix,
            df_sep='\t',
            header=None,
            is_utf8=True
        )
        results.columns = [
            'interact_id',
            'aa',
            'score'
        ]
        results['aa'] = results['aa'].astype(str)
        recombine = results[[
            'interact_id',
            'score'
        ]]
        return recombine

    def stkg(self):
        res = []
        for id in range(5):
            res_tool = self.dprs(
                dprs_path=self.RELEASE['sv_pred'],
                prot_name=self.RELEASE['prot_name'],
                file_chain=self.RELEASE['file_chain'],
                file_suffix='.m' + str(id + 1),
            )
            res_tool['placeholder'] = 0
            if id == 0:
                res.append(res_tool[['interact_id', 'placeholder', 'score']])
            else:
                res.append(res_tool[['score']])
        result = pd.concat([tt for tt in res], axis=1)
        seg_sep = phobius_dprs(
            self.RELEASE['phobius_path'],
            self.RELEASE['prot_name'],
            self.RELEASE['file_chain']
        ).read()
        if self.RELEASE['region'] == 'cytoplasmic':
            usl = self.xnovd2(seg_sep['cyto_lower'], seg_sep['cyto_upper'])
        elif self.RELEASE['region'] == 'extracellular':
            usl = self.xnovd2(seg_sep['extra_lower'], seg_sep['extra_upper'])
        elif self.RELEASE['region'] == 'transmembrane':
            usl = self.xnovd2(seg_sep['tmh_lower'], seg_sep['tmh_upper'])
        elif self.RELEASE['region'] == 'combined':
            usl = self.xnovd2(seg_sep['tmh_lower'], seg_sep['tmh_upper'])
        else:
            usl =self.usl
        return result.iloc[[i - 1 for i in np.squeeze(usl, 1)]].to_csv(
            self.RELEASE['sv_test_set'] + self.RELEASE['prot_name'] + self.RELEASE['file_chain'] + '.stk',
            sep=' ',
            header=None,
            index=False
        )

    def xnovd1(self, inf, sup):
        arr = []
        for i in range(inf, sup+1):
            arr.append([i])
        return arr

    def xnovd2(self, inf, sup):
        l = []
        for i in range(len(inf)):
            segment = self.xnovd1(inf[i], sup[i])
            for j in segment:
                l.append(j)
        return l

    def stkr(self):
        eclf_sv = joblib.load(self.RELEASE['model_fpn'])
        test_set = pd.read_csv(
            self.RELEASE['sv_test_set'] + self.RELEASE['prot_name'] + self.RELEASE['file_chain'] + '.stk',
            sep=' ',
            header=None
        )
        x_test = test_set.iloc[:, 2:]
        pred_data = eclf_sv.predict_proba(x_test)[:, [1]]
        ids = test_set.iloc[:, :1]
        seq_dict = kind_dprs().todict(self.sequence)
        ito = ids[0].tolist()
        ieo = []
        for ii in range(len(ids)):
            ieo.append(seq_dict[ito[ii]])
        pi = [ito, ieo]
        res = np.array(pi).T
        pred_data = np.concatenate((res, pred_data), axis=1)
        return pd.DataFrame(pred_data).to_csv(
            self.RELEASE['sv_pred'] + self.RELEASE['prot_name'] + self.RELEASE['file_chain'] + self.RELEASE['sv_suffix'],
            sep='\t',
            header=None,
            index=False
        )