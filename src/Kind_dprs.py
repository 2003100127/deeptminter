__author__ = "Jianfeng Sun"
__version__ = "v1.0"
__copyright__ = "Copyright 2020"
__license__ = "GPL v3.0"
__email__ = "jianfeng.sunmt@gmail.com"
__maintainer__ = "Jianfeng Sun"

import sys
sys.path.append('../')


class kind_dprs(object):

    def __init__(self, ):
        pass

    def todict(self, seq):
        seq_dict = {}
        len_seq = len(seq)
        for i in range(len_seq):
            seq_dict[i+1] = seq[i]
        return seq_dict