__author__ = "Jianfeng Sun"
__version__ = "v1.0"
__copyright__ = "Copyright 2025"
__license__ = "GPL v3.0"
__email__ = "jianfeng.sunmt@gmail.com"
__maintainer__ = "Jianfeng Sun"


class tinker:

    def fill(self, num, list_2d):
        list_2d_ = list_2d
        len_list_2d = len(list_2d_)
        for i in range(len_list_2d):
            list_2d_[i] = list_2d_[i] + [0 for _ in range(num)]
        return list_2d_