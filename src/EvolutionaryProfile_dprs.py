__author__ = "Jianfeng Sun"
__version__ = "v1.0"
__copyright__ = "Copyright 2020"
__license__ = "GPL v3.0"
__email__ = "jianfeng.sunmt@gmail.com"
__maintainer__ = "Jianfeng Sun"

import sys
import numpy as np
sys.path.append('../')
from src.FSingle_dprs import single_dprs


class evolutionaryProfile_dprs(object):

    def __init__(self, msa=None):
        if msa is not None:
            self.msa = msa
            self.ftgs = single_dprs(self.msa)

    def scheme1(self):
        fcmm = self.ftgs.columns()
        fre_msa = self.ftgs.alignment()
        fft = {}
        for aa in self.ftgs.aa_alphabet:
            if fre_msa[aa] == 0:
                fft[aa] = fcmm[aa] * 0
            else:
                fft[aa] = fcmm[aa] / fre_msa[aa]
        return fft

    def scheme2(self):
        fft = self.scheme1()
        for aa in self.ftgs.aa_alphabet:
            for j in range(len(fft['A'])):
                if fft[aa][j] == 0:
                    fft[aa][j] = 1
                else:
                    part = -np.log(fft[aa][j])
                    fft[aa][j] = 1 / (1 + np.exp(part))
        return fft

    def scheme2_(self, list_2d, window_aa_ids):
        list_2d_ = list_2d
        ep = self.scheme2()
        for i, aa_win_ids in enumerate(window_aa_ids):
            for j in aa_win_ids:
                for aa in self.ftgs.aa_alphabet:
                    if j is None:
                        list_2d_[i].append(0)
                    else:
                        list_2d_[i].append(ep[aa][j - 1])
        return list_2d_