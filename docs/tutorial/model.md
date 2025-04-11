# Model

## Tensorflow `2.19`
Download DeepTMInter's models.

::::{tab-set}
:::{tab-item} Command
:sync: tab1
```{code} python
import deeptminter

deeptminter.predict.download_data(
    url='https://github.com/2003100127/deeptminter/releases/download/model/model.zip',
    sv_fpn='../data/model.zip',
)
```
:::
:::{tab-item} Output
:sync: tab2
```shell
 ____                _____ __  __ ___       _            
|  _ \  ___  ___ _ _|_   _|  \/  |_ _|_ __ | |_ ___ _ __ 
| | | |/ _ \/ _ \ '_ \| | | |\/| || || '_ \| __/ _ \ '__|
| |_| |  __/  __/ |_) | | | |  | || || | | | ||  __/ |   
|____/ \___|\___| .__/|_| |_|  |_|___|_| |_|\__\___|_|   
                |_|                                      

05/04/2025 15:18:19 logger: =>Downloading starts...
05/04/2025 15:18:36 logger: =>downloaded.
```
:::
::::


You can download the models in shell.

::::{tab-set}
:::{tab-item} Command
:sync: tab1
```{code} shell
deeptminter_download -u https://github.com/2003100127/deeptminter/releases/download/model/model.zip -o ./data/deeptminter/model.zip
```
:::
:::{tab-item} Output
:sync: tab2
```{code} python
 ____                _____ __  __ ___       _            
|  _ \  ___  ___ _ _|_   _|  \/  |_ _|_ __ | |_ ___ _ __ 
| | | |/ _ \/ _ \ '_ \| | | |\/| || || '_ \| __/ _ \ '__|
| |_| |  __/  __/ |_) | | | |  | || || | | | ||  __/ |   
|____/ \___|\___| .__/|_| |_|  |_|___|_| |_|\__\___|_|   
                |_|                                      

06/04/2025 04:50:19 logger: =>Downloading starts...
06/04/2025 04:50:24 logger: =>downloaded.
```
:::
::::

The models contain 5 best-performing deep learning models and 1 stacking assembled model. In addition, we preserved models trained using tensorflow `1x`.