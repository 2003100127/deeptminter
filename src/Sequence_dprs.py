__author__ = "Jianfeng Sun"
__version__ = "v1.0"
__copyright__ = "Copyright 2020"
__license__ = "GPL v3.0"
__email__ = "jianfeng.sunmt@gmail.com"
__maintainer__ = "Jianfeng Sun"

import sys
sys.path.append('../')
from src.SSingle_dprs import single_dprs as ss


class sequence_dprs(object):
    def __init__(self, sequence):
        self.sequence = sequence
        self.aa = ss().get()

    def aac(self, ):
        aac_ = {}
        for _, i in enumerate(self.aa):
            aac_[i] = round(self.sequence.count(i) / len(self.sequence), 6)
        return aac_

    def aac_(self, list_2d, window_aa_names):
        list_2d_ = list_2d
        aac_dict = self.aac()
        for i, aa_win_ids in enumerate(window_aa_names):
            for j in aa_win_ids:
                if j is None:
                    for _ in range(20):
                        list_2d_[i].append(0)
                else:
                    for key, v in aac_dict.items():
                        list_2d_[i].append(v)
        return list_2d_