__author__ = "Jianfeng Sun"
__version__ = "v1.0"
__copyright__ = "Copyright 2020"
__license__ = "GPL v3.0"
__email__ = "jianfeng.sunmt@gmail.com"
__maintainer__ = "Jianfeng Sun"

import sys
sys.path.append('../')
import numpy as np
import pandas as pd


class phobius_dprs(object):

    def __init__(self, phobius_path, prot_name, file_chain):
        self.phobius_fpn = phobius_path + prot_name + file_chain + '.jphobius'

    def read(self):
        f = open(self.phobius_fpn)
        ctt = [[str(e) for e in line.split()] for line in f]
        ctt = pd.DataFrame(ctt)
        row_mark = ctt.loc[(ctt[0] == 'ID')].index[0]
        ctt = ctt.drop(index=np.arange(row_mark + 1))
        row_mark = ctt.loc[(ctt[0] == '//')].index[0]
        ctt = ctt.drop(index=[row_mark, row_mark + 1])
        ctt = ctt.reset_index(drop=True)
        ctt['type'] = ''
        if 4 not in ctt.columns:
            ctt[4] = None
        if 5 not in ctt.columns:
            ctt[5] = None
        for i in range(ctt.shape[0]):
            if ctt.iloc[i][4] is None:
                ctt.at[i, 4] = ''
            if ctt.iloc[i][5] is None:
                ctt.at[i, 5] = ''
            ctt.at[i, 'type'] = ctt.iloc[i][4] + ctt.iloc[i][5]
        ctt[2] = ctt[2].astype(np.int)
        ctt[3] = ctt[3].astype(np.int)
        isd = ctt[[2, 3]].loc[ctt['type'].isin(['CYTOPLASMIC.'])].values.tolist()
        tms = ctt[[2, 3]].loc[ctt[1].isin(['TRANSMEM'])].values.tolist()
        osd = ctt[[2, 3]].loc[ctt['type'].isin(['NONCYTOPLASMIC.'])].values.tolist()
        sg = ctt[[2, 3]].loc[ctt[1].isin(['SIGNAL'])].values.tolist()
        cr = ctt[[2, 3]].loc[ctt['type'].isin(['C-REGION.'])].values.tolist()
        hr = ctt[[2, 3]].loc[ctt['type'].isin(['H-REGION.'])].values.tolist()
        nr = ctt[[2, 3]].loc[ctt['type'].isin(['N-REGION.'])].values.tolist()
        cytoplasmic = self.format(isd)
        transmembrane = self.format(tms)
        extracellular = self.format(osd)
        sg = self.format(sg)
        cr = self.format(cr)
        hr = self.format(hr)
        nr = self.format(nr)
        phobius_dict = {
            'cyto_lower': cytoplasmic[0],
            'cyto_upper': cytoplasmic[1],
            'tmh_lower': transmembrane[0],
            'tmh_upper': transmembrane[1],
            'extra_lower': extracellular[0],
            'extra_upper': extracellular[1],
            'signal_lower': sg[0],
            'signal_upper': sg[1],
            'cregion_lower': cr[0],
            'cregion_upper': cr[1],
            'hregion_lower': hr[0],
            'hregion_upper': hr[1],
            'nregion_lower': nr[0],
            'nregion_upper': nr[1],
        }
        return phobius_dict

    def format(self, arr):
        lower = []
        upper = []
        for i in arr:
            lower.append(i[0])
            upper.append(i[1])
        return lower, upper

    def assign_(self, list_2d, window_aa_ids):
        list_2d_ = list_2d
        phobius_dict = self.read()
        for i, aa_win_ids in enumerate(window_aa_ids):
            for j in aa_win_ids:
                if j is None:
                    for _ in range(4):
                        list_2d_[i].append(0)
                else:
                    for m, x in enumerate(phobius_dict['cyto_lower']):
                        ic = pd.Interval(
                            left=x,
                            right=phobius_dict['cyto_upper'][m],
                            closed='both'
                        )
                        if j in ic:
                            list_2d_[i].append(0)
                            list_2d_[i].append(0)
                            list_2d_[i].append(0)
                            list_2d_[i].append(1)
                    for m, x in enumerate(phobius_dict['tmh_lower']):
                        it = pd.Interval(
                            left=x,
                            right=phobius_dict['tmh_upper'][m],
                            closed='both'
                        )
                        if j in it:
                            list_2d_[i].append(0)
                            list_2d_[i].append(0)
                            list_2d_[i].append(1)
                            list_2d_[i].append(0)
                    for m, x in enumerate(phobius_dict['extra_lower']):
                        ie = pd.Interval(
                            left=x,
                            right=phobius_dict['extra_upper'][m],
                            closed='both'
                        )
                        if j in ie:
                            list_2d_[i].append(0)
                            list_2d_[i].append(1)
                            list_2d_[i].append(0)
                            list_2d_[i].append(0)
                    for m, x in enumerate(phobius_dict['signal_lower']):
                        isg = pd.Interval(
                            left=x,
                            right=phobius_dict['signal_upper'][m],
                            closed='both'
                        )
                        if j in isg:
                            list_2d_[i].append(1)
                            list_2d_[i].append(0)
                            list_2d_[i].append(0)
                            list_2d_[i].append(0)
        return list_2d_