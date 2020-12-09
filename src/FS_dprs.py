__author__ = "Jianfeng Sun"
__version__ = "v1.0"
__copyright__ = "Copyright 2019"
__license__ = "GPL v3.0"
__email__ = "jianfeng.sunmt@gmail.com"
__maintainer__ = "Jianfeng Sun"

import sys
sys.path.append('../')
import numpy as np
from src.Single_dprs import single_dprs as wsingle
from src.Cumulative_dprs import cumulative_dprs as ecacmlt
from src.EvolutionaryProfile_dprs import evolutionaryProfile_dprs as ep
from src.Conservation_dprs import conservation_dprs
from src.AminoAcidProperty_dprs import aminoAcidProperty_dprs as aaprop
from src.Sequence_dprs import sequence_dprs as scomposition
from src.AminoAcidRep_dprs import aminoAcidRep_dprs as aarep
from src.MSA_dprs import msa_dprs as msaparser
from src.Phobius_dprs import phobius_dprs
from src.Reader_dprs import reader_dprs
from src.SSFasta_dprs import fasta_dprs as sfasta
from src.Fasta_dprs import fasta_dprs as pfasta
from src.Length_dprs import length_dprs as plength
from src.InformationTheory_dprs import informationTheory_dprs as it
from src.FSPosition_dprs import position_dprs as fposition
from src.Tinker_dprs import tinker


class fs_dprs(object):

    def __init__(self, RELEASE):
        self.read = reader_dprs()
        self.RELEASE = RELEASE

    def offone(self, list_2d, prot_name, file_chain, sequence, msa, window_aa_ids_1, window_aa_names_1, window_aa_ids_2, window_aa_names_2):
        fssa = list_2d
        len_seq = len(sequence)
        fssa = ecacmlt(
            sequence=sequence,
            window_size=self.RELEASE['window_size_2'],
            window_aa_ids=window_aa_ids_2
        ).assign(
            list_2d=fssa,
            prot_name=prot_name,
            file_chain=file_chain,
            L=len_seq,
            mi_path=self.RELEASE['mi_path'],
            fc_path=self.RELEASE['fc_path'],
            gdca_path=self.RELEASE['gdca_path'],
            cp_path=None,
            plmc_path=None,
            fc_activate=True,
            cp_activate=True,
            plmc_activate=True,
            gdca_activate=True,
            mi_activate=True,
        )
        fssa = phobius_dprs(
            phobius_path=self.RELEASE['phobius_path'],
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
        fssa = conservation_dprs(msa=msa).get_(
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

    def generate(self):
        print('Protein {} chain {} is being assembled.'.format(self.RELEASE['prot_name'], self.RELEASE['file_chain']))
        msa = msaparser(self.RELEASE['msa_path']+ self.RELEASE['prot_name']+ self.RELEASE['file_chain']+ '.aln').read()
        fasta_fpn = self.RELEASE['fasta_path']+ self.RELEASE['prot_name']+ self.RELEASE['file_chain']+ '.fasta'
        sequence = sfasta().getMerged(fasta_fpn)
        pos_list_single = plength().toSingle(len(sequence))
        position = pfasta(sequence).single(pos_list_single)
        window_aa_ids_1 = wsingle(
            sequence=sequence,
            position=position,
            window_size=self.RELEASE['window_size_1'],
        ).aaid()
        num_samples = len(window_aa_ids_1)
        window_aa_names_1 = wsingle(
            sequence=sequence,
            position=position,
            window_size=self.RELEASE['window_size_1'],
        ).aaname(window_aa_ids_1)
        window_aa_ids_2 = wsingle(
            sequence=sequence,
            position=position,
            window_size=self.RELEASE['window_size_2'],
        ).aaid()
        window_aa_names_2 = wsingle(
            sequence=sequence,
            position=position,
            window_size=self.RELEASE['window_size_2'],
        ).aaname(window_aa_ids_2)
        fss_ = [[] for _ in range(num_samples)]
        fss = self.offone(
            list_2d=fss_,
            prot_name=self.RELEASE['prot_name'],
            file_chain=self.RELEASE['file_chain'],
            sequence=sequence,
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
        f = open(self.RELEASE['sv_path']+ self.RELEASE['prot_name']+ self.RELEASE['file_chain']+ self.RELEASE['sv_suffix'], 'w')
        for i in ofd:
            k = ' '.join([str(j) for j in i])
            f.write(k + "\n")
        f.close()
        return 0