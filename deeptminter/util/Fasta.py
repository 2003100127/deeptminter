__author__ = "Jianfeng Sun"
__version__ = "v1.0"
__copyright__ = "Copyright 2025"
__license__ = "GPL v3.0"
__email__ = "jianfeng.sunmt@gmail.com"
__maintainer__ = "Jianfeng Sun"

from deeptminter.util.Sequence import Sequence


class Fasta:

    def __init__(self, sequence):
        self.sequence = sequence
        self.len_seq = len(self.sequence)

    def single(self, pos_list):
        seq_dict = Sequence(sequence=self.sequence).todict()
        len_pairs = len(pos_list)
        dist_matrix = []
        for i in range(len_pairs):
            fas_id1 = pos_list[i][0]
            dist_matrix.append([
                fas_id1,
                seq_dict[fas_id1],
                fas_id1,
                0
            ])
        return dist_matrix