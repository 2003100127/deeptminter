__author__ = "Jianfeng Sun"
__version__ = "v1.0"
__copyright__ = "Copyright 2020"
__license__ = "GPL v3.0"
__email__ = "jianfeng.sunmt@gmail.com"
__maintainer__ = "Jianfeng Sun"

import sys
sys.path.append('../')


class position_dprs(object):

    def __init__(self, ):
        pass

    def singlePosAbsolute_(self, list_2d, window_aa_ids, seq):
        list_2d_ = list_2d
        for i, aa_win_ids in enumerate(window_aa_ids):
            for j in aa_win_ids:
                if j is None:
                    list_2d_[i].append(0)
                else:
                    list_2d_[i].append(round(j / len(seq), 10))
        return list_2d_