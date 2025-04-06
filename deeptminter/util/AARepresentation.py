__author__ = "Jianfeng Sun"
__version__ = "v1.0"
__copyright__ = "Copyright 2025"
__license__ = "GPL v3.0"
__email__ = "jianfeng.sunmt@gmail.com"
__maintainer__ = "Jianfeng Sun"

from deeptminter.util.SSingle import SSingle


class AARepresentation:
    
    def __init__(self, ):
        self.aa_dict = SSingle().todict(gap=False)
        
    def onehot(self, list_2d, window_aa_names):
        list_2d_ = list_2d
        for i, aa_win_names in enumerate(window_aa_names):
            for j in aa_win_names:
                if j is None:
                    for k in range(20):
                        list_2d_[i].append(0)
                else:
                    bool_ = [0] * 20
                    bool_[self.aa_dict[j]] = 1
                    for k in range(20):
                        list_2d_[i].append(bool_[k])
        return list_2d_