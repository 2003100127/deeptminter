__author__ = "Jianfeng Sun"
__version__ = "v1.0"
__copyright__ = "Copyright 2020"
__license__ = "GPL v3.0"
__email__ = "jianfeng.sunmt@gmail.com"
__maintainer__ = "Jianfeng Sun"

import sys
sys.path.append('../')
import numpy as np
from src.FSingle_dprs import single_dprs


class informationTheory_dprs(object):
    
    def __init__(self, msa):
        self.msa = msa
        self.sf = single_dprs(self.msa)

    def entropy(self, ):
        ent = dict()
        freq_column = self.sf.columns()
        len_seq = len(freq_column['A'])
        for i in range(len_seq):
            tmp = 0
            for aa in self.sf.aa_alphabet:
                if freq_column[aa][i] != 0:
                    tmp = tmp + freq_column[aa][i] * np.log10(freq_column[aa][i])
            ent[i + 1] = -tmp * 2
        return ent

    def entropy_(self, list_2d, window_aa_ids):
        list_2d_ = list_2d
        ent_dict = self.entropy()
        for i, aa_win_ids in enumerate(window_aa_ids):
            for j in aa_win_ids:
                if j is None:
                    list_2d_[i].append(0)
                else:
                    list_2d_[i].append(ent_dict[j])
        return list_2d_