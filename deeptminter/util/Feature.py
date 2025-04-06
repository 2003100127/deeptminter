__author__ = "Jianfeng Sun"
__version__ = "v1.0"
__copyright__ = "Copyright 2025"
__license__ = "GPL v3.0"
__email__ = "jianfeng.sunmt@gmail.com"
__maintainer__ = "Jianfeng Sun"

import numpy as np
from deeptminter.util.WSingle import WSingle as wsingle
from deeptminter.util.Cumulative import Cumulative as ecacmlt
from deeptminter.util.EvolutionaryProfile import EvolutionaryProfile as ep
from deeptminter.util.Conservation import Conservation as conservation
from deeptminter.util.AAProperty import AAProperty as aaprop
from deeptminter.util.Sequence import Sequence as scomposition
from deeptminter.util.AARepresentation import AARepresentation as aarep
from deeptminter.util.MSA import MSA as msaparser
from deeptminter.util.Phobius import Phobius as phobius
from deeptminter.util.Fasta import Fasta as pfasta
from deeptminter.util.Length import Length as plength
from deeptminter.util.InformationTheory import InformationTheory as it
from deeptminter.util.FSPosition import FSPosition as fposition
from deeptminter.util.Tinker import tinker
from deeptminter.util.Console import Console


class Feature:

    def __init__(
            self,
            params,
            verbose=True,
    ):
        self.params = params

        self.console = Console()
        self.console.verbose = verbose

    def offone(
            self,
            list_2d,
            prot_name,
            file_chain,
            sequence,
            msa,
            window_aa_ids_1,
            window_aa_names_1,
            window_aa_ids_2,
            window_aa_names_2,
    ):
        fssa = list_2d
        len_seq = len(sequence)
        fssa = ecacmlt(
            sequence=sequence,
            window_size=4,
            window_aa_ids=window_aa_ids_2
        ).assign(
            list_2d=fssa,
            prot_name=prot_name,
            file_chain=file_chain,
            L=len_seq,
            mi_path=self.params['mi_fp'],
            fc_path=self.params['fc_fp'],
            gdca_path=self.params['gdca_fp'],
            cp_path=None,
            plmc_path=None,
            fc_activate=True,
            cp_activate=True,
            plmc_activate=True,
            gdca_activate=True,
            mi_activate=True,
        )
        fssa = phobius(
            phobius_path=self.params['phobius_fp'],
            prot_name=prot_name,
            file_chain=file_chain
        ).assign_(
            list_2d=fssa,
            window_aa_ids=window_aa_ids_1,
        )
        fssa = aaprop().get_(
            list_2d=fssa,
            window_aa_names=window_aa_names_2
        )
        fssa = it(msa=msa).entropy_(
            list_2d=fssa,
            window_aa_ids=window_aa_ids_1
        )
        fssa = aarep().onehot(
            list_2d=fssa,
            window_aa_names=window_aa_names_1
        )
        fssa = conservation(msa=msa).get_(
            list_2d=fssa,
            window_aa_ids=window_aa_ids_1
        )
        fssa = fposition().singlePosAbsolute_(
            list_2d=fssa,
            window_aa_ids=window_aa_ids_1,
            seq=sequence
        )
        fssa = ep(msa=msa).scheme2_(
            list_2d=fssa,
            window_aa_ids=window_aa_ids_2
        )
        fssa = scomposition(sequence=sequence).aac_(
            list_2d=fssa,
            window_aa_names=window_aa_names_1
        )
        fssa = tinker().fill(
            num=13,
            list_2d=fssa
        )
        return fssa

    def generate(self, ):
        self.console.print('======>Features are being assembled...')
        msa = msaparser(self.params['msa_fp']+ self.params['prot_name']+ self.params['file_chain']+ '.aln').read()
        pos_list_single = plength().toSingle(len(self.params['sequence']))
        position = pfasta(self.params['sequence']).single(pos_list_single)
        window_aa_ids_1 = wsingle(
            sequence=self.params['sequence'],
            position=position,
            window_size=1,
        ).aaid()
        num_samples = len(window_aa_ids_1)
        window_aa_names_1 = wsingle(
            sequence=self.params['sequence'],
            position=position,
            window_size=1,
        ).aaname(window_aa_ids_1)
        window_aa_ids_2 = wsingle(
            sequence=self.params['sequence'],
            position=position,
            window_size=4,
        ).aaid()
        window_aa_names_2 = wsingle(
            sequence=self.params['sequence'],
            position=position,
            window_size=4,
        ).aaname(window_aa_ids_2)
        fss_ = [[] for _ in range(num_samples)]
        fss = self.offone(
            list_2d=fss_,
            prot_name=self.params['prot_name'],
            file_chain=self.params['file_chain'],
            sequence=self.params['sequence'],
            msa=msa,
            window_aa_ids_1=window_aa_ids_1,
            window_aa_names_1=window_aa_names_1,
            window_aa_ids_2=window_aa_ids_2,
            window_aa_names_2=window_aa_names_2
        )
        fss = np.array(fss).astype(np.float64)
        lll = np.zeros((num_samples, 2))
        lll[np.arange(num_samples), len(position) * [0]] = 1
        ofd = np.concatenate((fss, lll), axis=1)
        if self.params['sv_fp']:
            f = open(self.params['sv_fp']+ self.params['prot_name']+ self.params['file_chain']+ self.params['sv_suffix'], 'w')
            for i in ofd:
                k = ' '.join([str(j) for j in i])
                f.write(k + "\n")
            f.close()
        self.console.print('======>Finished being assembled.')
        return ofd