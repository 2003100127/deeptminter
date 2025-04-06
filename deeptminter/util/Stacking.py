__author__ = "Jianfeng Sun"
__version__ = "v1.0"
__copyright__ = "Copyright 2025"
__license__ = "GPL v3.0"
__email__ = "jianfeng.sunmt@gmail.com"
__maintainer__ = "Jianfeng Sun"

import joblib
import numpy as np
import pandas as pd
from deeptminter.util.Reader import Reader as pfreader
from deeptminter.util.SSFasta import SSFasta as sfasta
from deeptminter.util.Sequence import Sequence
from deeptminter.util.Length import Length as plength
from deeptminter.util.Phobius import Phobius as phobius
from deeptminter.util.Console import Console


class Stacking:

    def __init__(
            self,
            params=None,
    ):
        self.params = params
        self.pfreader = pfreader()
        self.sequence = sfasta().get(
            fasta_fpn=self.params['fasta_fp'] + self.params['prot_name'] + self.params['file_chain'] + '.fasta',
        )
        self.usl = plength().toSingle(len(self.sequence))

    def read_isite(self, isite_fp, prot_name, file_chain, file_suffix):
        results = self.pfreader.generic(
            isite_fp + prot_name + file_chain + file_suffix,
            df_sep='\t',
            header=None,
            is_utf8=True
        )
        results.columns = [
            'interact_id',
            'aa',
            'score'
        ]
        results['aa'] = results['aa'].astype(str)
        recombine = results[[
            'interact_id',
            'score'
        ]]
        return recombine

    def stkg(self):
        res = []
        for id in range(5):
            res_tool = self.read_isite(
                isite_fp=self.params['isite_fp'],
                prot_name=self.params['prot_name'],
                file_chain=self.params['file_chain'],
                file_suffix='.m' + str(id + 1),
            )
            res_tool['placeholder'] = 0
            if id == 0:
                res.append(res_tool[['interact_id', 'placeholder', 'score']])
            else:
                res.append(res_tool[['score']])
        result = pd.concat([tt for tt in res], axis=1)
        seg_sep = phobius(
            self.params['phobius_fp'],
            self.params['prot_name'],
            self.params['file_chain']
        ).read()
        if self.params['region'] == 'cytoplasmic':
            usl = self.xnovd2(seg_sep['cyto_lower'], seg_sep['cyto_upper'])
        elif self.params['region'] == 'extracellular':
            usl = self.xnovd2(seg_sep['extra_lower'], seg_sep['extra_upper'])
        elif self.params['region'] == 'transmembrane':
            usl = self.xnovd2(seg_sep['tmh_lower'], seg_sep['tmh_upper'])
        elif self.params['region'] == 'combined':
            usl = self.xnovd2(seg_sep['tmh_lower'], seg_sep['tmh_upper'])
        else:
            usl =self.usl
        return result.iloc[[i - 1 for i in np.squeeze(usl, 1)]].to_csv(
            self.params['sv_fp_stacking_input'] + self.params['prot_name'] + self.params['file_chain'] + '.stk',
            sep=' ',
            header=None,
            index=False
        )

    def xnovd1(self, inf, sup):
        arr = []
        for i in range(inf, sup+1):
            arr.append([i])
        return arr

    def xnovd2(self, inf, sup):
        l = []
        for i in range(len(inf)):
            segment = self.xnovd1(inf[i], sup[i])
            for j in segment:
                l.append(j)
        return l

    def stkr(
            self,
            verbose=True,
    ):
        console = Console()
        console.verbose = verbose
        eclf_sv = joblib.load(self.params['model_fpn'])
        # print(eclf_sv)
        test_set = pd.read_csv(
            self.params['sv_fp_stacking_input'] + self.params['prot_name'] + self.params['file_chain'] + '.stk',
            sep=' ',
            header=None,
        )
        x_test = test_set.iloc[:, 2:]
        n_features = x_test.shape[1]

        # to patch _var
        for name, est in eclf_sv.named_estimators_.items():
            if name == 'ada':
                n_classes = len(est.classes_)
                if not hasattr(est, "var_"):
                    est.var_ = np.ones((n_classes, n_features))
                if not hasattr(est, "theta_"):
                    est.theta_ = np.zeros((n_classes, n_features))
                if not hasattr(est, "sigma_"):
                    est.sigma_ = est.var_

        # to patch _label_encoder
        if not hasattr(eclf_sv, "_label_encoder"):
            from sklearn.preprocessing import LabelEncoder
            le = LabelEncoder()
            le.classes_ = eclf_sv.classes_
            eclf_sv._label_encoder = le

        pred_data = eclf_sv.predict_proba(x_test)[:, [1]]
        # print(pred_data)
        ids = test_set.iloc[:, :1]
        seq_dict = Sequence(sequence=self.sequence).todict()
        ito = ids[0].tolist()
        ieo = []
        for ii in range(len(ids)):
            ieo.append(seq_dict[ito[ii]])
        pi = [ito, ieo]
        res = np.array(pi).T
        pred_data = np.concatenate((res, pred_data), axis=1)
        df = pd.DataFrame(pred_data)
        console.print('Predictions are: \n{}'.format(df))
        if self.params['sv_fp']:
            df.to_csv(
                self.params['sv_fp'] + self.params['prot_name'] + self.params['file_chain'] + self.params['sv_suffix'],
                sep='\t',
                header=False,
                index=False
            )
        console.print('Finished!')
        return df