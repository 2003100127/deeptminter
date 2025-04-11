# Data

## Input

### External tools

Protein sequences are only needed for running DeepTMInter, and are also used to generate a list of intermediate files before running DeepTMInter, as shown in [Table 1](#tbl:external-tool).

:::{note} Fasta
:class: dropdown
Protein sequences in [the Fasta format](https://en.wikipedia.org/wiki/FASTA_format) are required. The file extension must be `.fasta` for recognition of the software.
:::

:::{table} External tools for generating intermediate files before running DeepTMInter.
:label: tbl:external-tool
:align: center

|                              Tool                              |     Role     |                Function                 |                     Source                     |
|:--------------------------------------------------------------:|:------------:|:---------------------------------------:|:----------------------------------------------:|
|       [HHblits](https://github.com/soedinglab/hh-suite)        |    Input     | generating multiple sequence alignments |      <https://doi.org/10.1038/nmeth.1818>      |
|  [Gaussian DCA](https://github.com/carlobaldassi/GaussDCA.jl)  |    Input     |      predictor of residue contacts      | <https://doi.org/10.1371/journal.pone.0092721> |
| [Freecontact](https://rostlab.org/owiki/index.php/FreeContact) |    Input     |      predictor of residue contacts      |   <https://doi.org/10.1186/1471-2105-15-85>    |
|         [Phobius](http://phobius.sbc.su.se/data.html)          |    Input     |  predictor of transmembrane topologies  |  <https://doi.org/10.1016/j.jmb.2004.03.016>   |
|      [Uniclust30 database](https://uniclust.mmseqs.com/)       | Intermediate |            sequence database            |     <https://doi.org/10.1093/nar/gkw1081>      |

:::

:::{tip}
`troll.sh` is used to generate multiple sequence alignments, transmembrane topologies, and all of evolutionary coupling features including [EVfold](https://doi.org/10.1371/journal.pone.0028766) (generated using FreeContact) and Gaussian DCA.
:::

## Output files

DeepTMInter finally returns an output file with the suffix of `.m1`, `.m2`, `.m3`, `.m4`, `.m5` or `.deeptminter`.

Predictions of interaction sites in tansmembrane proteins are shown in the output file, with three columns: 

1. positions of animo acids in the input sequence
2. animo acids
3. probabilities of being interaction sites

:::{tip}
Please note that if you have a sequence sharing a high sequence identity to the proteins in the _TrainData_ dataset (please check our [Mendeley Data](https://data.mendeley.com/datasets/2t8kgwzp35/2) @Sun2021deeptminterdata), we recommend any of the three suffixes `.mexpand1`, `.mexpand2`, or `.mexpand3` denoted in your project.
:::

If you want to get the results in the context of no ideally preferred regions predicted by Phobius. You can set `-r` as `combined` to run the program. This will return the predictions of the whole fasta sequence. Then, you can tailor the whole predictions to whatever you want.


## Example data

Users can download some example data and check an assortment of input files.

::::{tab-set}
:::{tab-item} Code
:sync: tab1
```{code} python
import deeptminter

deeptminter.predict.download_data(
    url='https://github.com/2003100127/deeptminter/releases/download/example_data/example_data.zip',
    sv_fpn='../data/example_data.zip',
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

05/04/2025 15:27:20 logger: =>Downloading starts...
05/04/2025 15:27:21 logger: =>downloaded.
```
:::
::::

