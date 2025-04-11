# Prediction

## Overview

You need to decompress the `example_data.zip` file in your preferred folder, e.g., `deeptminter/`.

:::{caution} Model declaration
We primarily use models in Tensorflow `2x` to perform predictions.
:::

## Deep learning for interaction site prediction


### Python

We define several parameters required for running . 

```{code} python
params = {
    'prot_name': '3jcu',
    'prot_chain': 'H',
    'fasta_fp': '../../data/deeptminter/example_data/',
    'msa_fp': '../../data/deeptminter/example_data/',
    'phobius_fp': '../../data/deeptminter/example_data/',
    'mi_fp': '../../data/deeptminter/example_data/',
    'fc_fp': '../../data/deeptminter/example_data/',
    'gdca_fp': '../../data/deeptminter/example_data/',
    'sv_fp_feature': '../../data/deeptminter/example_data/',
    'sv_suffix_feature': '.f',

    'model_frozen_fpn': '../../data/deeptminter/model/tf2/frozen_graph/m1.pb',
    'batch_size': 100,
    'sv_fp_pred': '../../data/deeptminter/',
    'sv_suffix_pred': '.m1',
}
```

::::{tab-set}
:::{tab-item} Code
:sync: tab1
```{code} python
import deeptminter

deeptminter.predict.isite(
    prot_name=params['prot_name'],
    prot_chain=params['prot_chain'],
    fasta_fp=params['fasta_fp'],
    msa_fp=params['msa_fp'],
    phobius_fp=params['phobius_fp'],
    mi_fp=params['mi_fp'],
    fc_fp=params['fc_fp'],
    gdca_fp=params['gdca_fp'],
    sv_fp_feature=params['sv_fp_feature'],
    sv_suffix_feature=params['sv_suffix_feature'],
    model_frozen_fpn=params['model_frozen_fpn'],
    sv_fp_pred=params['sv_fp_pred'],
    sv_suffix_pred=params['sv_suffix_pred'],
    batch_size=100,
    verbose=True,
)
```
:::
:::{tab-item} Output
:sync: tab2
```{code} shell
 ____                _____ __  __ ___       _            
|  _ \  ___  ___ _ _|_   _|  \/  |_ _|_ __ | |_ ___ _ __ 
| | | |/ _ \/ _ \ '_ \| | | |\/| || || '_ \| __/ _ \ '__|
| |_| |  __/  __/ |_) | | | |  | || || | | | ||  __/ |   
|____/ \___|\___| .__/|_| |_|  |_|___|_| |_|\__\___|_|   
                |_|                                      

05/04/2025 16:00:51 logger: ===>Protein: 3jcu chain: H
05/04/2025 16:00:51 logger: ======>Features are being assembled...
05/04/2025 16:00:51 logger: ======>Finished being assembled.
05/04/2025 16:00:51 logger: ===>The model (../../data/deeptminter/model/tf2/frozen_graph/m1.pb) with frozen graphs converted from tensorflow 1.15.2 is being read...
05/04/2025 16:00:53 logger: ======>Predicted probabilities of interation sites:
     0  1           2
0    1  P  0.44524422
1    2  K   0.5642183
2    3  P  0.57570034
...
57  58  S  0.53011745
58  59  M   0.3377973
05/04/2025 16:00:53 logger: ======>Predictions are saved to ../../data/deeptminter/3jcuH.m1
```
:::
::::


### CLI

DeepTMInter can also be used in shell. To know how to use, please type

```{code} shell
deeptminter -h
```

It shows the usage of different parameters.

```{code} shell
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
```

You can run it using the following code.

::::{tab-set}
:::{tab-item} Command
:sync: tab1
```{code} shell
deeptminter -pn 3jcu -pc H -fa ./data/deeptminter/example_data/ -msafp ./data/deeptminter/example_data/ -phobfp ./data/deeptminter/example_data/ -mifp ./data/deeptminter/example_data/ -fcfp ./data/deeptminter/example_data/ -gdcafp ./data/deeptminter/example_data/ -m ./data/deeptminter/model/tf2/frozen_graph/m1.pb -sv_fp_f ./data/deeptminter/example_data/ -sv_suf_f .f -sv_fp_p ./data/deeptminter/ -sv_suf_p .m1 -bs 100
```
:::
:::{tab-item} Output
:sync: tab2
```{code} shell
  ____                _____ __  __ ___       _
|  _ \  ___  ___ _ _|_   _|  \/  |_ _|_ __ | |_ ___ _ __
| | | |/ _ \/ _ \ '_ \| | | |\/| || || '_ \| __/ _ \ '__|
| |_| |  __/  __/ |_) | | | |  | || || | | | ||  __/ |
|____/ \___|\___| .__/|_| |_|  |_|___|_| |_|\__\___|_|
                |_|

05/04/2025 16:11:18 logger: ===>Protein: 3jcu chain: H
05/04/2025 16:11:18 logger: ======>Features are being assembled...
05/04/2025 16:11:19 logger: ======>Finished being assembled.
05/04/2025 16:11:19 logger: ===>The model (./data/deeptminter/model/tf2/frozen_graph/m1.pb) with frozen graphs converted from tensorflow 1.15.2 is being read...
05/04/2025 16:11:20 logger: ===>The model is read in, with
05/04/2025 16:11:20 logger: ======>Predicted probabilities of interation sites:
     0  1           2
0    1  P  0.44524422
1    2  K   0.5642183
2    3  P  0.57570034
...
57  58  S  0.53011745
58  59  M   0.3377973
05/04/2025 16:11:20 logger: ======>Predictions are saved to ./data/deeptminter/3jcuH.m1
```
:::
::::

## Assembled prediction

If you'd like to explore if better predictions can be gained from assembled methods, you can generate models by choosing to run the running code.

### Python

First, we define parameters for input and output.

```{code} python
params_stacking = {
    'prot_name': '3jcu',
    'prot_chain': 'H',
    'region': 'combined',
    'fasta_fp': '../../data/deeptminter/example_data/',
    'phobius_fp': '../../data/deeptminter/example_data/',
    'isite_fp': '../../data/deeptminter/',

    'model_fpn': '../../data/deeptminter/model/stacking.model',
    'sv_fp_stacking_input': '../../data/deeptminter/',
    'sv_fp': '../../data/deeptminter/',
    'sv_suffix': '.deeptminter'
}
```

Then, we performed predictions.

::::{tab-set}
:::{tab-item} Command
:sync: tab1
```{code} python
import deeptminter

deeptminter.predict.stacking(
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
```
:::
:::{tab-item} Output
:sync: tab2
```{code} shell
 ____                _____ __  __ ___       _            
|  _ \  ___  ___ _ _|_   _|  \/  |_ _|_ __ | |_ ___ _ __ 
| | | |/ _ \/ _ \ '_ \| | | |\/| || || '_ \| __/ _ \ '__|
| |_| |  __/  __/ |_) | | | |  | || || | | | ||  __/ |   
|____/ \___|\___| .__/|_| |_|  |_|___|_| |_|\__\___|_|   
                |_|                                      

05/04/2025 16:33:23 logger: ===>Protein: 3jcu chain: H
05/04/2025 16:33:23 logger: Predictions are: 
     0  1                   2
0   29  L  0.6798641623872085
1   30  M  0.6557471888350399
2   31  G  0.6949745997232504
...
19  48  Y  0.7044071371080728
20  49  N   0.705696071814507
05/04/2025 16:33:23 logger: Finished!
```
:::
::::


### CLI

DeepTMInter can also be used in shell. To know how to use, please type

::::{tab-set}
:::{tab-item} Command
:sync: tab1
```{code} shell
deeptminter_assemble -pn 3jcu -pc H -fa ./data/deeptminter/example_data/ -phobfp ./data/deeptminter/example_data/ -m ./data/deeptminter/model/stacking.model -ifp ./data/deeptminter/ -r combined -sv_fp_s ./data/deeptminter/ -sv_fp ./data/deeptminter/ -sv_suf .deeptminter
```
:::
:::{tab-item} Output
:sync: tab2
```{code} shell
 ____                _____ __  __ ___       _
|  _ \  ___  ___ _ _|_   _|  \/  |_ _|_ __ | |_ ___ _ __
| | | |/ _ \/ _ \ '_ \| | | |\/| || || '_ \| __/ _ \ '__|
| |_| |  __/  __/ |_) | | | |  | || || | | | ||  __/ |
|____/ \___|\___| .__/|_| |_|  |_|___|_| |_|\__\___|_|
                |_|

05/04/2025 16:42:07 logger: ===>Protein: 3jcu chain: H
05/04/2025 16:42:08 logger: Predictions are:
     0  1                   2
0   29  L  0.6798641623872085
1   30  M  0.6557471888350399
2   31  G  0.6949745997232504
3   32  V  0.6678435513228781
4   33  A  0.4116563950495269
5   34  M  0.6756479650668131
6   35  A  0.3599768716465631
7   36  L  0.5715904491452858
8   37  F  0.7324822410039901
9   38  A  0.4415552709397562
10  39  V  0.6785871628435665
11  40  F  0.5630136567015621
12  41  L  0.6344924489703325
13  42  S  0.7063788778070768
14  43  I  0.6599980449464243
15  44  I  0.6579266981626475
16  45  L  0.7058936221993016
17  46  E   0.639440562706253
18  47  I  0.6948413389284585
19  48  Y  0.7044071371080728
20  49  N   0.705696071814507
05/04/2025 16:42:08 logger: Finished!
```
:::
::::