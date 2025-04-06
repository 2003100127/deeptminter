__author__ = "Jianfeng Sun"
__version__ = "v1.0"
__copyright__ = "Copyright 2025"
__license__ = "GPL v3.0"
__email__ = "jianfeng.sunmt@gmail.com"
__maintainer__ = "Jianfeng Sun"


class WSingle:

    def __init__(self, sequence, position, window_size):
        self.sequence = sequence
        self.aa = position
        self.window_size = window_size
        self.len_seq = len(self.sequence)

    def aaid(self):
        num_aa = len(self.aa)
        aai = [[] for _ in range(num_aa)]
        for i in range(num_aa):
            for il in range(self.window_size):
                aai[i].append(self.aa[i][0] - (self.window_size - il))
            aai[i].append(self.aa[i][0])
            for ir in range(self.window_size):
                aai[i].append(self.aa[i][0] + (ir + 1))
        for i in range(len(aai)):
            for j in range(len(aai[0])):
                if aai[i][j] < 1 or aai[i][j] > len(self.sequence):
                    aai[i][j] = None
        return aai

    def aaname(self, aa_idices):
        num_aa = len(aa_idices)
        aan = [[] for _ in range(num_aa)]
        for i in range(len(aa_idices)):
            for j in range(len(aa_idices[0])):
                if aa_idices[i][j] is None:
                    aan[i].append(None)
                for k, character in enumerate(self.sequence):
                    if aa_idices[i][j] == k + 1:
                        aan[i].append(character)
        return aan