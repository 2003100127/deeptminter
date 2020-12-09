__author__ = "Jianfeng Sun"
__version__ = "v1.0"
__copyright__ = "Copyright 2020"
__license__ = "GPL v3.0"
__email__ = "jianfeng.sunmt@gmail.com"
__maintainer__ = "Jianfeng Sun"

import sys
sys.path.append('../')
from src.Position_dprs import position_dprs


class length_dprs(position_dprs):

    def __init__(self, seq_sep_inferior=None, seq_sep_superior=None):
        super(length_dprs, self).__init__(seq_sep_inferior, seq_sep_superior)

    def toSingle(self, length):
        return self.num2arr1d(1, length)

    def num2arr1d(self, inf, sup):
        arr = []
        for i in range(inf, sup+1):
            arr.append([i])
        return arr