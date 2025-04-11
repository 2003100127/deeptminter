# Installation

## Overview

We tested **DeepTMInter** on a Linux operating system, as several input feature generation tools are Linux-dependent. However, if you already have the required feature files (as shown in [example_data](./tutorial/data#Input)), the program can be run on other platforms such as Windows and macOS. Before using the software, please ensure that Python (version `>=3.11`) is installed. We highly recommend using [Anaconda](https://www.anaconda.com/), an integrated Python development environment, which simplifies package management and environment setup.

## Installing

### GitHub

Then, we can follow the step-by-step precedures for installation.

Step 1: Get the most recent version of **DeepTMInter** from GitHub (_clone it at your preferred location_), PyPI, or Conda.

```shell
git clone https://github.com/2003100127/deeptminter.git
```

Step 2: Create a conda environment in your local machine.

```shell
conda create --name deeptminter python=3.12

conda activate deeptminter
```

Step 3: install via pip

::::{tab-set}
:::{tab-item} Command
:sync: tab1
```shell
cd deeptminter

pip install .
```
:::
:::{tab-item} Log
:sync: tab2
```{code} shell
  Installing build dependencies ... done
  Getting requirements to build wheel ... done
  Preparing metadata (pyproject.toml) ... done
Requirement already satisfied: biopython<2.0,>=1.85 in d:\programming\anaconda3\envs\deeptminter\lib\site-packages (from deeptminter==0.0.1) (1.85)
Requirement already satisfied: click<9.0.0,>=8.1.8 in d:\programming\anaconda3\envs\deeptminter\lib\site-packages (from deeptminter==0.0.1) (8.1.8)
Requirement already satisfied: joblib==1.4.2 in d:\programming\anaconda3\envs\deeptminter\lib\site-packages (from deeptminter==0.0.1) (1.4.2)
Requirement already satisfied: numpy==2.1.3 in d:\programming\anaconda3\envs\deeptminter\lib\site-packages (from deeptminter==0.0.1) (2.1.3)
Requirement already satisfied: pandas==2.2.3 in d:\programming\anaconda3\envs\deeptminter\lib\site-packages (from deeptminter==0.0.1) (2.2.3)
Requirement already satisfied: pyfiglet<2.0.0,>=1.0.2 in d:\programming\anaconda3\envs\deeptminter\lib\site-packages (from
deeptminter==0.0.1) (1.0.2)
Requirement already satisfied: scikit-learn<2.0.0,>=1.6.1 in d:\programming\anaconda3\envs\deeptminter\lib\site-packages (from deeptminter==0.0.1) (1.6.1)
Requirement already satisfied: tensorflow==2.19 in d:\programming\anaconda3\envs\deeptminter\lib\site-packages (from deeptminter==0.0.1) (2.19.0)
Requirement already satisfied: python-dateutil>=2.8.2 in d:\programming\anaconda3\envs\deeptminter\lib\site-packages (from
pandas==2.2.3->deeptminter==0.0.1) (2.9.0.post0)
Requirement already satisfied: pytz>=2020.1 in d:\programming\anaconda3\envs\deeptminter\lib\site-packages (from pandas==2.2.3->deeptminter==0.0.1) (2025.2)
Requirement already satisfied: tzdata>=2022.7 in d:\programming\anaconda3\envs\deeptminter\lib\site-packages (from pandas==2.2.3->deeptminter==0.0.1) (2025.2)
Requirement already satisfied: absl-py>=1.0.0 in d:\programming\anaconda3\envs\deeptminter\lib\site-packages (from tensorflow==2.19->deeptminter==0.0.1) (2.2.2)
Requirement already satisfied: astunparse>=1.6.0 in d:\programming\anaconda3\envs\deeptminter\lib\site-packages (from tensorflow==2.19->deeptminter==0.0.1) (1.6.3)
Requirement already satisfied: flatbuffers>=24.3.25 in d:\programming\anaconda3\envs\deeptminter\lib\site-packages (from tensorflow==2.19->deeptminter==0.0.1) (25.2.10)
Requirement already satisfied: gast!=0.5.0,!=0.5.1,!=0.5.2,>=0.2.1 in d:\programming\anaconda3\envs\deeptminter\lib\site-packages (from tensorflow==2.19->deeptminter==0.0.1) (0.6.0)
Requirement already satisfied: google-pasta>=0.1.1 in d:\programming\anaconda3\envs\deeptminter\lib\site-packages (from tensorflow==2.19->deeptminter==0.0.1) (0.2.0)
Requirement already satisfied: libclang>=13.0.0 in d:\programming\anaconda3\envs\deeptminter\lib\site-packages (from tensorflow==2.19->deeptminter==0.0.1) (18.1.1)
Requirement already satisfied: opt-einsum>=2.3.2 in d:\programming\anaconda3\envs\deeptminter\lib\site-packages (from tensorflow==2.19->deeptminter==0.0.1) (3.4.0)
Requirement already satisfied: packaging in d:\programming\anaconda3\envs\deeptminter\lib\site-packages (from tensorflow==2.19->deeptminter==0.0.1) (24.2)
Requirement already satisfied: protobuf!=4.21.0,!=4.21.1,!=4.21.2,!=4.21.3,!=4.21.4,!=4.21.5,<6.0.0dev,>=3.20.3 in d:\programming\anaconda3\envs\deeptminter\lib\site-packages (from tensorflow==2.19->deeptminter==0.0.1) (5.29.4)
Requirement already satisfied: requests<3,>=2.21.0 in d:\programming\anaconda3\envs\deeptminter\lib\site-packages (from tensorflow==2.19->deeptminter==0.0.1) (2.32.3)
Requirement already satisfied: setuptools in d:\programming\anaconda3\envs\deeptminter\lib\site-packages (from tensorflow==2.19->deeptminter==0.0.1) (78.1.0)
Requirement already satisfied: six>=1.12.0 in d:\programming\anaconda3\envs\deeptminter\lib\site-packages (from tensorflow==2.19->deeptminter==0.0.1) (1.17.0)
Requirement already satisfied: termcolor>=1.1.0 in d:\programming\anaconda3\envs\deeptminter\lib\site-packages (from tensorflow==2.19->deeptminter==0.0.1) (3.0.1)
Requirement already satisfied: typing-extensions>=3.6.6 in d:\programming\anaconda3\envs\deeptminter\lib\site-packages (from tensorflow==2.19->deeptminter==0.0.1) (4.13.1)
Requirement already satisfied: wrapt>=1.11.0 in d:\programming\anaconda3\envs\deeptminter\lib\site-packages (from tensorflow==2.19->deeptminter==0.0.1) (1.17.2)
Requirement already satisfied: grpcio<2.0,>=1.24.3 in d:\programming\anaconda3\envs\deeptminter\lib\site-packages (from tensorflow==2.19->deeptminter==0.0.1) (1.71.0)
Requirement already satisfied: tensorboard~=2.19.0 in d:\programming\anaconda3\envs\deeptminter\lib\site-packages (from tensorflow==2.19->deeptminter==0.0.1) (2.19.0)
Requirement already satisfied: keras>=3.5.0 in d:\programming\anaconda3\envs\deeptminter\lib\site-packages (from tensorflow==2.19->deeptminter==0.0.1) (3.9.2)
Requirement already satisfied: h5py>=3.11.0 in d:\programming\anaconda3\envs\deeptminter\lib\site-packages (from tensorflow==2.19->deeptminter==0.0.1) (3.13.0)
Requirement already satisfied: ml-dtypes<1.0.0,>=0.5.1 in d:\programming\anaconda3\envs\deeptminter\lib\site-packages (from tensorflow==2.19->deeptminter==0.0.1) (0.5.1)
Requirement already satisfied: colorama in d:\programming\anaconda3\envs\deeptminter\lib\site-packages (from click<9.0.0,>=8.1.8->deeptminter==0.0.1) (0.4.6)
Requirement already satisfied: scipy>=1.6.0 in d:\programming\anaconda3\envs\deeptminter\lib\site-packages (from scikit-learn<2.0.0,>=1.6.1->deeptminter==0.0.1) (1.15.2)
Requirement already satisfied: threadpoolctl>=3.1.0 in d:\programming\anaconda3\envs\deeptminter\lib\site-packages (from scikit-learn<2.0.0,>=1.6.1->deeptminter==0.0.1) (3.6.0)
Requirement already satisfied: wheel<1.0,>=0.23.0 in d:\programming\anaconda3\envs\deeptminter\lib\site-packages (from astunparse>=1.6.0->tensorflow==2.19->deeptminter==0.0.1) (0.45.1)
Requirement already satisfied: rich in d:\programming\anaconda3\envs\deeptminter\lib\site-packages (from keras>=3.5.0->tensorflow==2.19->deeptminter==0.0.1) (14.0.0)
Requirement already satisfied: namex in d:\programming\anaconda3\envs\deeptminter\lib\site-packages (from keras>=3.5.0->tensorflow==2.19->deeptminter==0.0.1) (0.0.8)
Requirement already satisfied: optree in d:\programming\anaconda3\envs\deeptminter\lib\site-packages (from keras>=3.5.0->tensorflow==2.19->deeptminter==0.0.1) (0.14.1)
Requirement already satisfied: charset-normalizer<4,>=2 in d:\programming\anaconda3\envs\deeptminter\lib\site-packages (from requests<3,>=2.21.0->tensorflow==2.19->deeptminter==0.0.1) (3.4.1)
Requirement already satisfied: idna<4,>=2.5 in d:\programming\anaconda3\envs\deeptminter\lib\site-packages (from requests<3,>=2.21.0->tensorflow==2.19->deeptminter==0.0.1) (3.10)
Requirement already satisfied: urllib3<3,>=1.21.1 in d:\programming\anaconda3\envs\deeptminter\lib\site-packages (from requests<3,>=2.21.0->tensorflow==2.19->deeptminter==0.0.1) (2.3.0)
Requirement already satisfied: certifi>=2017.4.17 in d:\programming\anaconda3\envs\deeptminter\lib\site-packages (from requests<3,>=2.21.0->tensorflow==2.19->deeptminter==0.0.1) (2025.1.31)
Requirement already satisfied: markdown>=2.6.8 in d:\programming\anaconda3\envs\deeptminter\lib\site-packages (from tensorboard~=2.19.0->tensorflow==2.19->deeptminter==0.0.1) (3.7)
Requirement already satisfied: tensorboard-data-server<0.8.0,>=0.7.0 in d:\programming\anaconda3\envs\deeptminter\lib\site-packages (from tensorboard~=2.19.0->tensorflow==2.19->deeptminter==0.0.1) (0.7.2)
Requirement already satisfied: werkzeug>=1.0.1 in d:\programming\anaconda3\envs\deeptminter\lib\site-packages (from tensorboard~=2.19.0->tensorflow==2.19->deeptminter==0.0.1) (3.1.3)
Requirement already satisfied: MarkupSafe>=2.1.1 in d:\programming\anaconda3\envs\deeptminter\lib\site-packages (from werkzeug>=1.0.1->tensorboard~=2.19.0->tensorflow==2.19->deeptminter==0.0.1) (3.0.2)
Requirement already satisfied: markdown-it-py>=2.2.0 in d:\programming\anaconda3\envs\deeptminter\lib\site-packages (from rich->keras>=3.5.0->tensorflow==2.19->deeptminter==0.0.1) (3.0.0)
Requirement already satisfied: pygments<3.0.0,>=2.13.0 in d:\programming\anaconda3\envs\deeptminter\lib\site-packages (from rich->keras>=3.5.0->tensorflow==2.19->deeptminter==0.0.1) (2.19.1)
Requirement already satisfied: mdurl~=0.1 in d:\programming\anaconda3\envs\deeptminter\lib\site-packages (from markdown-it-py>=2.2.0->rich->keras>=3.5.0->tensorflow==2.19->deeptminter==0.0.1) (0.1.2)
Building wheels for collected packages: deeptminter
  Building wheel for deeptminter (pyproject.toml) ... done
  Created wheel for deeptminter: filename=deeptminter-0.0.1-py3-none-any.whl size=41958 sha256=8ba60451b9fa1a37c25703831be770e536369eae887d86b573858f228e3a2ef8
  Stored in directory: C:\Users\jianf\AppData\Local\Temp\pip-ephem-wheel-cache-mgxlclhm\wheels\3c\e2\cf\fb72fde24eb11ec52379f120902d40206490def08ae52b7f6e
Successfully built deeptminter
Installing collected packages: deeptminter
  Attempting uninstall: deeptminter
    Found existing installation: deeptminter 0.0.1
    Uninstalling deeptminter-0.0.1:
      Successfully uninstalled deeptminter-0.0.1
Successfully installed deeptminter-0.0.1
```
:::
::::

Everything should be all set before you run **DeepTMInter**.