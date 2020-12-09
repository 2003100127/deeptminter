__author__ = "Jianfeng Sun"
__version__ = "v1.0"
__copyright__ = "Copyright 2020"
__license__ = "GPL v3.0"
__email__ = "jianfeng.sunmt@gmail.com"
__maintainer__ = "Jianfeng Sun"

import os
import sys
import getopt
import subprocess
from src.FS_dprs import fs_dprs
from src.Stacking_dprs import stacking_dprs


def usage():
    return """
    DeepTMInter: improving prediction of interaction sites in transmembrane protein.

    Usage: run_deeptminter.py [-n|--name, [sequence name']] [-c|--chain, [sequence chain name]] [-i|--input, [input path]] [-o|--output, [output path]] [-r|--region, [region]] [-h|--help] [-v|--version]

    Description
                -n, --name      Sequence name. For example, '3jcu'.
                -c, --chain     Sequence chain name. For example, 'H'. This can be empty if you prefer a sequnce name like '3jcuH' or '0868'.
                -i, --input     Input path.
                -o, --output    Output path.
                -r, --region    region of transmembrane protein. It can take 'transmembrane', 'cytoplasmic', 'extracellular', 'combined'.

    for example:
    python run_deeptminter.py -n 3jcu -c H -i ./input/ -o ./output/ -r transmembrane

    """


def parser():
    opts, args = getopt.getopt(sys.argv[1:], '-h-n:-c:-i:-o:-r:-v',
                               ['help', 'name=', 'chain=', 'input=', 'output=', 'region=', 'version'])
    # print(opts)
    for opt_name, opt_value in opts:
        if opt_name in ('-h', '--help'):
            print(usage())
            sys.exit(0)
        if opt_name in ('-v', '--version'):
            print("*Version: 1.0")
        if opt_name in ('-n', '--name'):
            seq_name = opt_value
        if opt_name in ('-c', '--chain'):
            seq_chain = opt_value
        if opt_name in ('-i', '--input'):
            input = opt_value
        if opt_name in ('-o', '--output'):
            output = opt_value
        if opt_name in ('-r', '--region'):
            region = opt_value
        # else:
        #     print('wrong usage.')
        #     sys.exit(0)
    return seq_name, seq_chain, input, output, region

seq_name, seq_chain, input_path, output_path, region = parser()

# seq_name = '3jcu'
# seq_chain = 'H'
# input_path = './input/'
# output_path = './output/'
# region = 'extracellular'

fs_in = {
    'prot_name': seq_name,
    'file_chain': seq_chain,
    'window_size_1': 1,
    'window_size_2': 4,
    'fasta_path': input_path,
    'msa_path': input_path,
    'phobius_path': input_path,
    'mi_path': input_path,
    'fc_path': input_path,
    'cp_path': input_path,
    'plmc_path': input_path,
    'gdca_path': input_path,
    'sv_suffix': '.fs',
    'sv_path': input_path,
}
fs_dprs(fs_in).generate()


m1_in = [
    "python",
    os.path.join(os.path.dirname(os.path.abspath(__file__)), 'deeptminter_call.py'),
    os.path.join(os.path.dirname(os.path.abspath(__file__)), 'model/m1/m1.meta'),
    os.path.join(os.path.dirname(os.path.abspath(__file__)), 'model/m1/m1'),
    seq_name,
    seq_chain,
    input_path,
    output_path,
    '.fs',
    '.m1',
]
subprocess.Popen(m1_in, shell=True).communicate()

m2_in = [
    "python",
    os.path.join(os.path.dirname(os.path.abspath(__file__)), 'deeptminter_call.py'),
    os.path.join(os.path.dirname(os.path.abspath(__file__)), 'model/m2/m2.meta'),
    os.path.join(os.path.dirname(os.path.abspath(__file__)), 'model/m2/m2'),
    seq_name,
    seq_chain,
    input_path,
    output_path,
    '.fs',
    '.m2',
]
subprocess.Popen(m2_in, shell=True).communicate()

m3_in = [
    "python",
    os.path.join(os.path.dirname(os.path.abspath(__file__)), 'deeptminter_call.py'),
    os.path.join(os.path.dirname(os.path.abspath(__file__)), 'model/m3/m3.meta'),
    os.path.join(os.path.dirname(os.path.abspath(__file__)), 'model/m3/m3'),
    seq_name,
    seq_chain,
    input_path,
    output_path,
    '.fs',
    '.m3',
]
subprocess.Popen(m3_in, shell=True).communicate()

m4_in = [
    "python",
    os.path.join(os.path.dirname(os.path.abspath(__file__)), 'deeptminter_call.py'),
    os.path.join(os.path.dirname(os.path.abspath(__file__)), 'model/m4/m4.meta'),
    os.path.join(os.path.dirname(os.path.abspath(__file__)), 'model/m4/m4'),
    seq_name,
    seq_chain,
    input_path,
    output_path,
    '.fs',
    '.m4',
]
subprocess.Popen(m4_in, shell=True).communicate()

m5_in = [
    "python",
    os.path.join(os.path.dirname(os.path.abspath(__file__)), 'deeptminter_call.py'),
    os.path.join(os.path.dirname(os.path.abspath(__file__)), 'model/m5/m5.meta'),
    os.path.join(os.path.dirname(os.path.abspath(__file__)), 'model/m5/m5'),
    seq_name,
    seq_chain,
    input_path,
    output_path,
    '.fs',
    '.m5',
]
subprocess.Popen(m5_in, shell=True).communicate()

mexpand1_in = [
    "python",
    os.path.join(os.path.dirname(os.path.abspath(__file__)), 'deeptminter_call.py'),
    os.path.join(os.path.dirname(os.path.abspath(__file__)), 'model/mexpand1/mexpand1.meta'),
    os.path.join(os.path.dirname(os.path.abspath(__file__)), 'model/mexpand1/mexpand1'),
    seq_name,
    seq_chain,
    input_path,
    output_path,
    '.fs',
    '.mexpand1',
]
subprocess.Popen(mexpand1_in, shell=True).communicate()

mexpand2_in = [
    "python",
    os.path.join(os.path.dirname(os.path.abspath(__file__)), 'deeptminter_call.py'),
    os.path.join(os.path.dirname(os.path.abspath(__file__)), 'model/mexpand2/mexpand2.meta'),
    os.path.join(os.path.dirname(os.path.abspath(__file__)), 'model/mexpand2/mexpand2'),
    seq_name,
    seq_chain,
    input_path,
    output_path,
    '.fs',
    '.mexpand2',
]
subprocess.Popen(mexpand2_in, shell=True).communicate()

mexpand3_in = [
    "python",
    os.path.join(os.path.dirname(os.path.abspath(__file__)), 'deeptminter_call.py'),
    os.path.join(os.path.dirname(os.path.abspath(__file__)), 'model/mexpand3/mexpand3.meta'),
    os.path.join(os.path.dirname(os.path.abspath(__file__)), 'model/mexpand3/mexpand3'),
    seq_name,
    seq_chain,
    input_path,
    output_path,
    '.fs',
    '.mexpand3',
]
subprocess.Popen(mexpand3_in, shell=True).communicate()


stk_in = {
    'prot_name': seq_name,
    'file_chain': seq_chain,
    'region': region,
    'sv_test_set': output_path,
    'input_path': input_path,
    'phobius_path': input_path,
    'model_fpn': os.path.join(os.path.dirname(os.path.abspath(__file__)), 'model/ensemble.model'),
    'sv_pred': output_path,
    'sv_suffix': '.deeptminter'
}
stk = stacking_dprs(stk_in)
stk.stkg()
stk.stkr()