__author__ = "Jianfeng Sun"
__version__ = "v1.0"
__copyright__ = "Copyright 2025"
__license__ = "GPL v3.0"
__email__ = "jianfeng.sunmt@gmail.com"
__maintainer__ = "Jianfeng Sun"

import pandas as pd


class Reader:

    def generic(self, df_fpn, df_sep='\t', header=None, is_utf8=False):
        if is_utf8:
            return pd.read_csv(df_fpn, sep=df_sep, header=header, encoding='utf-8')
        else:
            return pd.read_csv(df_fpn, sep=df_sep, header=header)