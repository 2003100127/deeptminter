__author__ = "Jianfeng Sun"
__version__ = "v1.0"
__copyright__ = "Copyright 2020"
__license__ = "GPL v3.0"
__email__ = "jianfeng.sunmt@gmail.com"
__maintainer__ = "Jianfeng Sun"

import sys
sys.path.append('../')


class msa_dprs(object):

    def __init__(self, msa_fpn):
        self.msa_fpn = msa_fpn

    def read(self):
        read_msa = open(self.msa_fpn, 'r')
        results = list()
        for line in read_msa.readlines():
            line = line.strip()
            if not len(line) or line.startswith('#'):
                continue
            results.append(line)
        return results