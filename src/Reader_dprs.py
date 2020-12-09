__author__ = "Jianfeng Sun"
__version__ = "v1.0"
__copyright__ = "Copyright 2020"
__license__ = "GPL v3.0"
__email__ = "jianfeng.sunmt@gmail.com"
__maintainer__ = "Jianfeng Sun"

import sys
sys.path.append('../')
import pandas as pd


class reader_dprs(object):

    def __init__(self, ):
        pass

    def generic(self, df_fpn, df_sep='\t', header=None, is_utf8=False):
        if is_utf8:
            return pd.read_csv(df_fpn, sep=df_sep, header=header, encoding='utf-8')
        else:
            return pd.read_csv(df_fpn, sep=df_sep, header=header)