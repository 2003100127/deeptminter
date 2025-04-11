# Versions

## Change

::::{grid} 2 2 2 2

|  Version  |                                  Date                                   |
|:---------:|:-----------------------------------------------------------------------:|
| 2021-2024 |   ![](https://img.shields.io/badge/past_released-March._2021-red.svg)   |
|  `0.0.1`  | ![](https://img.shields.io/badge/latest_released-April._2025-green.svg) |

::::

## Before `0.0.1`

The version of **DeepTMInter** released in 2021 can only be run on the Tensorflow `1x` platform.

### Inference

```{code} shell
python run_deeptminter.py -n 3jcu -c H -i ./input/ -o ./output/ -r transmembrane
```

```{code} shell
-n --name -> a sequence name. For example, '3jcu'.
-c --chain -> a chain name. For example, 'H'. This can be empty if you prefer a sequnce name like '3jcuH' or '0868'.
-i --input -> input path
-o --output --> prediction results
-r, --region --> region of transmembrane protein. It can take 'transmembrane', 'cytoplasmic', 'extracellular', 'combined', 'all where 'combined' means accumulation of 'transmembrane', 'cytoplasmic', 'extracellular'. 'all' means the whole fasta sequence.

```