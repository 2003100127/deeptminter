__author__ = "Jianfeng Sun"
__version__ = "v1.0"
__copyright__ = "Copyright 2025"
__license__ = "GPL v3.0"
__email__ = "jianfeng.sunmt@gmail.com"
__maintainer__ = "Jianfeng Sun"

import click
import urllib.request
from pyfiglet import Figlet
import numpy as np
import pandas as pd
import tensorflow as tf
from deeptminter import load
from deeptminter.util.Feature import Feature
from deeptminter.util.DataInitializer import DataInitializer
from deeptminter.util.SSFasta import SSFasta as sfasta
from deeptminter.util.Fasta import Fasta as pfasta
from deeptminter.util.Length import Length as lscenario
from deeptminter.util.Stacking import Stacking
from deeptminter.util.Console import Console


vignette1 = Figlet(font='standard')

CONTEXT_SETTINGS = dict(help_option_names=['-h', '--help'])


@click.command(short_help=vignette1.renderText('DeepTMInter'), context_settings=CONTEXT_SETTINGS)
@click.option('-u', '--url', default='https://github.com/2003100127/deeptminter/releases/download/model/model.zip', help='URL of deeptminter models')
@click.option('-o', '--sv_fpn', default='./model.zip', help='output path of deeptminter models')
def download(url, sv_fpn):
    download_data(url, sv_fpn)


def download_data(
        url,
        sv_fpn,
        verbose=True,
):
    console = Console()
    console.verbose = verbose
    print(vignette1.renderText('DeepTMInter'))
    console.print('=>Downloading starts...')
    urllib.request.urlretrieve(
        url=url,
        filename=sv_fpn
    )
    console.print('=>downloaded.')
    return 'downloaded.'


class HelpfulCmd(click.Command):
    def format_help(self, ctx, formatter):
        click.echo(vignette1.renderText('DeepTMInter'))
        click.echo(
            '''
            Options:
            -pn, --prot_name, Name of the protein to be processed.
            -pc, --prot_chain, Chain ID of the protein (e.g., A, B, etc.).
            -fa, --fasta_fp, File path to the input FASTA sequence.
            -msafp, --msa_fp, File path to the multiple sequence alignment (MSA).
            -phobfp, --phobius_fp, File path to the Phobius output file.
            -mifp, --mi_fp, File path to the mutual information (MI) data.
            -fcfp, --fc_fp, File path to the FreeContact (FC) data.
            -gdcafp, --gdca_fp, File path to the direct coupling analysis (DCA) output.
            -m, --model_frozen_fpn, Path to the frozen model (.pb) file for prediction.
            -sv_fp_f, --sv_fp_feature, Path to the feature vector for interaction site prediction.
            -sv_suf_f, --sv_suffix_feature, Suffix for feature files used in interaction site input.
            -sv_fp_p, --sv_fp_pred, Output file path for predicted results.
            -sv_suf_p, --sv_suffix_pred, Suffix for predicted output files.
            -bs, --batch_size, Batch size used during prediction (default: 100).
            -vb, --verbose, Whether to print detailed logs during processing (default: True).
            '''
        )


@click.command(cls=HelpfulCmd, context_settings=CONTEXT_SETTINGS)
@click.option('-pn', '--prot_name', required=True, help='Name of the protein to be processed.')
@click.option('-pc', '--prot_chain', required=True, help='Chain ID of the protein (e.g., A, B, etc.).')
@click.option('-fa', '--fasta_fp', required=True, help='File path to the input FASTA sequence.')
@click.option('-msafp', '--msa_fp', required=True, help='File path to the multiple sequence alignment (MSA).')
@click.option('-phobfp', '--phobius_fp', required=True, help='File path to the Phobius output file.')
@click.option('-mifp', '--mi_fp', required=True, help='File path to the mutual information (MI) data.')
@click.option('-fcfp', '--fc_fp', required=True, help='File path to the FreeContact (FC) data.')
@click.option('-gdcafp', '--gdca_fp', required=True, help='File path to the direct coupling analysis (DCA) output.')
@click.option('-m', '--model_frozen_fpn', required=True, help='Path to the frozen model (.pb) file for prediction.')
@click.option('-sv_fp_f', '--sv_fp_feature', default='./', help='Path to the feature vector for interaction site prediction.')
@click.option('-sv_suf_f', '--sv_suffix_feature', default='.f', help='Suffix for feature files used in interaction site input.')
@click.option('-sv_fp_p', '--sv_fp_pred', default='./', help='Output file path for predicted results.')
@click.option('-sv_suf_p', '--sv_suffix_pred', default='.deeptminter', help='Suffix for predicted output files.')
@click.option('-bs', '--batch_size', default=100, help='Batch size used during prediction (default: 100).')
@click.option('-vb', '--verbose', default=True, help='Whether to print detailed logs during processing (default: True).')
def isite_(
        prot_name,
        prot_chain,
        fasta_fp,
        msa_fp,
        phobius_fp,
        mi_fp,
        fc_fp,
        gdca_fp,
        sv_fp_feature,
        sv_suffix_feature,
        model_frozen_fpn,
        sv_fp_pred,
        sv_suffix_pred,
        batch_size,
        verbose,
):
    isite(
        prot_name=prot_name,
        prot_chain=prot_chain,
        fasta_fp=fasta_fp,
        msa_fp=msa_fp,
        phobius_fp=phobius_fp,
        mi_fp=mi_fp,
        fc_fp=fc_fp,
        gdca_fp=gdca_fp,
        sv_fp_feature=sv_fp_feature,
        sv_suffix_feature=sv_suffix_feature,
        model_frozen_fpn=model_frozen_fpn,
        sv_fp_pred=sv_fp_pred,
        sv_suffix_pred=sv_suffix_pred,
        batch_size=batch_size,
        verbose=verbose,
    )


def isite(
        prot_name,
        prot_chain,
        fasta_fp,
        msa_fp,
        phobius_fp,
        mi_fp,
        fc_fp,
        gdca_fp,
        sv_fp_feature,
        sv_suffix_feature,
        model_frozen_fpn,
        sv_fp_pred,
        sv_suffix_pred,
        batch_size=100,
        verbose=True,
):
    console = Console()
    console.verbose = verbose

    print(vignette1.renderText('DeepTMInter'))

    console.print("===>Protein: {} chain: {}".format(prot_name, prot_chain))

    sequence = sfasta().get(fasta_fpn=fasta_fp + prot_name + prot_chain + '.fasta')

    mat_np = Feature(params={
        'prot_name': prot_name,
        'file_chain': prot_chain,
        'sequence': sequence,
        'msa_fp': msa_fp,
        'phobius_fp': phobius_fp,
        'mi_fp': mi_fp,
        'fc_fp': fc_fp,
        'gdca_fp': gdca_fp,
        'sv_fp': sv_fp_feature,
        'sv_suffix': sv_suffix_feature,
    }).generate()
    # print(mat_np)

    x_test, y_test, num_test_samples = DataInitializer().input2d(
        data=mat_np,
        bound_inf=676,
        bound_sup=-2,
    )

    console.print("===>The model ({}) with frozen graphs converted from tensorflow 1.15.2 is being read...".format(model_frozen_fpn))
    graph = load.frozen_graph(model_frozen_fpn)
    x_tf = graph.get_tensor_by_name("x_1:0")
    pred_tf = graph.get_tensor_by_name("presoftmax:0")
    console.print("===>The model is read in, with\ninput: {}\noutput: {}".format(x_tf, pred_tf))
    sess = tf.compat.v1.Session(graph=graph)

    accumulator = []
    num_batch_test = num_test_samples // batch_size
    final_number = num_test_samples % batch_size
    for batch in range(num_batch_test + 1):
        if batch < num_batch_test:
            x_batch_te, y_batch_te = DataInitializer().batchData(
                x_test, y_test, batch, batch_size
            )
        else:
            x_batch_te = x_test[batch*batch_size: (batch*batch_size+final_number), :]
        feed_dict_test = {x_tf: x_batch_te}
        pred_tmp = sess.run(pred_tf, feed_dict=feed_dict_test)
        accumulator.append(pred_tmp)
    pred_data = accumulator[0]
    for i in range(1, len(accumulator)):
        pred_data = np.concatenate((pred_data, accumulator[i]), axis=0)
    # print(pred_data)

    length_pos_list = lscenario().toSingle(len(sequence))
    position = pfasta(sequence).single(pos_list=length_pos_list)
    res = np.array(position)[:, [0, 1]]
    pred_data = np.concatenate((res, pred_data[:, [1]]), axis=1)
    df = pd.DataFrame(pred_data)
    console.print("======>Predicted probabilities of interation sites:\n{}".format(df))
    if sv_fp_pred:
        sv_fpn_pred = sv_fp_pred + prot_name + prot_chain + sv_suffix_pred
        df.to_csv(
            sv_fpn_pred,
            sep='\t',
            header=False,
            index=False
        )
        console.print("======>Predictions are saved to {}".format(sv_fpn_pred))
    return df


class HelpfulCmds(click.Command):
    def format_help(self, ctx, formatter):
        click.echo(vignette1.renderText('DeepTMInter'))
        click.echo(
            '''
            Options:
            -pn, --prot_name, name of the protein to be processed
            -pc, --prot_chain, chain ID of the protein (e.g., A, B, etc.)
            -fa, --fasta_fp, file path to the input FASTA sequence
            -phobfp, --phobius_fp, file path to the Phobius output file
            -m, --model_fpn, path to the model (joblib) file for prediction
            -ifp, --isite_fp, path to interaction site predictions (default: ./)
            -r, --region, region to focus on: cytoplasmic, extracellular, transmembrane, or combined (default: combined)
            -sv_fp_s, --sv_fp_stacking_input, path to stacking input features (default: ./)
            -sv_fp, --sv_fp, output file path for predicted results (default: ./)
            -sv_suf, --sv_suffix, suffix for predicted output files (default: .deeptminter)
            -vb, --verbose, whether to print detailed logs during processing (default: True)
            '''
        )


@click.command(cls=HelpfulCmds, context_settings=CONTEXT_SETTINGS)
@click.option('-pn', '--prot_name', required=True, help='Name of the protein to be processed.')
@click.option('-pc', '--prot_chain', required=True, help='Chain ID of the protein (e.g., A, B, etc.).')
@click.option('-fa', '--fasta_fp', required=True, help='File path to the input FASTA sequence.')
@click.option('-phobfp', '--phobius_fp', required=True, help='File path to the Phobius output file.')
@click.option('-m', '--model_fpn', required=True, help='Path to the model (job) file for prediction.')
@click.option('-ifp', '--isite_fp', default='./', help='Path to interaction site predictions.')
@click.option('-r', '--region', default='combined', help='region: cytoplasmic, extracellular, transmembrane, or combined')
@click.option('-sv_fp_s', '--sv_fp_stacking_input', default='./', help='Path to stacking input.')
@click.option('-sv_fp', '--sv_fp', default='./', help='Output file path for predicted results.')
@click.option('-sv_suf', '--sv_suffix', default='.deeptminter', help='Suffix for predicted output files.')
@click.option('-vb', '--verbose', default=True, help='Whether to print detailed logs during processing (default: True).')
def stacking_(
        prot_name,
        prot_chain,
        region,
        fasta_fp,
        phobius_fp,
        isite_fp,
        sv_fp_stacking_input,
        model_fpn,
        sv_fp,
        sv_suffix,
        verbose,
):
    return stacking(
        prot_name=prot_name,
        prot_chain=prot_chain,
        region=region,
        fasta_fp=fasta_fp,
        phobius_fp=phobius_fp,
        isite_fp=isite_fp,
        sv_fp_stacking_input=sv_fp_stacking_input,
        model_fpn=model_fpn,
        sv_fp=sv_fp,
        sv_suffix=sv_suffix,
        verbose=verbose,
)

def stacking(
        prot_name,
        prot_chain,
        region,
        fasta_fp,
        phobius_fp,
        isite_fp,
        sv_fp_stacking_input,
        model_fpn,
        sv_fp,
        sv_suffix,
        verbose=True,
):
    console = Console()
    console.verbose = verbose
    print(vignette1.renderText('DeepTMInter'))

    console.print("===>Protein: {} chain: {}".format(prot_name, prot_chain))
    stk_in = {
        'prot_name': prot_name,
        'file_chain': prot_chain,
        'region': region,
        'fasta_fp': fasta_fp,
        'phobius_fp': phobius_fp,
        'isite_fp': isite_fp,
        'sv_fp_stacking_input': sv_fp_stacking_input,
        'model_fpn': model_fpn,
        'sv_fp': sv_fp,
        'sv_suffix': sv_suffix,
    }
    stk = Stacking(stk_in)
    stk.stkg()
    stk.stkr()


if __name__ == "__main__":
    # download data
    # download_data(
    #     # url='https://github.com/2003100127/deeptminter/releases/download/model/model.zip',
    #     # sv_fpn='../data/model.zip',
    #     url='https://github.com/2003100127/deeptminter/releases/download/example_data/example_data.zip',
    #     sv_fpn='../data/example_data.zip',
    # )

    params = {
        'prot_name': '3jcu',
        'prot_chain': 'H',
        'fasta_fp': '../data/input/',
        'msa_fp': '../data/input/',
        'phobius_fp': '../data/input/',
        'mi_fp': '../data/input/',
        'fc_fp': '../data/input/',
        'gdca_fp': '../data/input/',
        'sv_fp_feature': '../data/input/',
        'sv_suffix_feature': '.f',

        'model_frozen_fpn': '../data/model/tf2/frozen_graph/m4.pb',
        'batch_size': 100,
        # 'sv_fp_pred': '../data/output/refurbished/',
        'sv_fp_pred': '../data/output/sss/',
        'sv_suffix_pred': '.m4',
    }
    # isite(
    #     prot_name=params['prot_name'],
    #     prot_chain=params['prot_chain'],
    #     fasta_fp=params['fasta_fp'],
    #     msa_fp=params['msa_fp'],
    #     phobius_fp=params['phobius_fp'],
    #     mi_fp=params['mi_fp'],
    #     fc_fp=params['fc_fp'],
    #     gdca_fp=params['gdca_fp'],
    #     sv_fp_feature=params['sv_fp_feature'],
    #     sv_suffix_feature=params['sv_suffix_feature'],
    #     model_frozen_fpn=params['model_frozen_fpn'],
    #     sv_fp_pred=params['sv_fp_pred'],
    #     sv_suffix_pred=params['sv_suffix_pred'],
    #     batch_size=100,
    #     verbose=True,
    # )

    params_stacking = {
        'prot_name': '3jcu',
        'prot_chain': 'H',
        'region': '111', # 'transmembrane', 'cytoplasmic', 'extracellular', 'combined'.
        'fasta_fp': '../data/input/',
        'phobius_fp': '../data/input/',
        'isite_fp': '../data/output/refurbished/',

        'model_fpn': '../data/model/stacking.model',
        # 'sv_fp_stacking_input': '../data/output/refurbished/',
        'sv_fp_stacking_input': '../data/output/sss/',
        # 'sv_fp': '../data/output/refurbished/',
        'sv_fp': '../data/output/sss/',
        'sv_suffix': '.deeptminter'
    }
    stacking(
        prot_name=params_stacking['prot_name'],
        prot_chain=params_stacking['prot_chain'],
        region=params_stacking['region'],
        fasta_fp=params_stacking['fasta_fp'],
        phobius_fp=params_stacking['phobius_fp'],
        isite_fp=params_stacking['isite_fp'],
        sv_fp_stacking_input=params_stacking['sv_fp_stacking_input'],
        model_fpn=params_stacking['model_fpn'],
        sv_fp=params_stacking['sv_fp'],
        sv_suffix=params_stacking['sv_suffix'],
    )