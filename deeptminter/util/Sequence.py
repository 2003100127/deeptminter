__author__ = "Jianfeng Sun"
__version__ = "v1.0"
__copyright__ = "Copyright 2025"
__license__ = "GPL v3.0"
__email__ = "jianfeng.sunmt@gmail.com"
__maintainer__ = "Jianfeng Sun"

from deeptminter.util.SSingle import SSingle


class Sequence:

    def __init__(
            self,
            sequence,
    ):
        self.sequence = sequence
        self.aa = SSingle().get()

    def todict(self, ):
        seq_dict = {}
        len_seq = len(self.sequence)
        for i in range(len_seq):
            seq_dict[i+1] = self.sequence[i]
        return seq_dict

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