__author__ = "Jianfeng Sun"
__version__ = "v1.0"
__copyright__ = "Copyright 2020"
__license__ = "GPL v3.0"
__email__ = "jianfeng.sunmt@gmail.com"
__maintainer__ = "Jianfeng Sun"

import sys
sys.path.append('../')
import numpy as np
from src.InformationTheory_dprs import informationTheory_dprs


class conservation_dprs(object):
    
    def __init__(self, msa=None, thres=20):
        self.msa = msa
        self.thres = thres

    def get(self, ):
        ent = informationTheory_dprs(msa=self.msa).entropy()
        conser = {}
        for k, v in ent.items():
            conser[k] = 1 - (v / np.log(self.thres))
        return conser

    def get_(self, list_2d, window_aa_ids):
        list_2d_ = list_2d
        ent_dict = self.get()
        for i, aa_win_ids in enumerate(window_aa_ids):
            for j in aa_win_ids:
                if j is None:
                    list_2d_[i].append(0)
                else:
                    list_2d_[i].append(ent_dict[j])
        return list_2d_