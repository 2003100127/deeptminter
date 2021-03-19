# DeepTMInter
![](https://img.shields.io/badge/DeepTMInter-executable-519dd9.svg)
![](https://img.shields.io/badge/last_released_date-Dec._2020-green.svg)

###### tags: `transmembrane protein` `predicting interaction sites` `v1.0`


<!-- > :information_source::warning: <span style="color:red">**NOTE:**</span> Ten supplementary tables (19-28 :point_up:) in Excel format for the paper titled "Improved sequence-based prediction of interaction sites in α-helical transmembrane proteins by deep learning" are available at folder [./data/](https://github.com/2003100127/deeptminter/tree/master/data) :exclamation:and [mendeley](https://data.mendeley.com/drafts/2t8kgwzp35):exclamation:. -->
:information_source: News: The DeepTMInter Docker software has become available at [deeptminter/releases](https://github.com/2003100127/deeptminter/releases). Please see below.
## Overview
This repository is a software package of DeepTMInter. DeepTMInter is a deep-learning-based approach and it was developed using stacked generalization ensembles of ultradeep residual neural networks. The approach shows a substantial improvement for predicting interaction sites in transmembrane proteins compared to existing methods. All training and benchmarked data are available [here](https://data.mendeley.com/datasets/2t8kgwzp35/1) and other data are made available upon requests of users via [email](mailto:jianfeng.sunmt@gmail.com).

## System Requirement
We tested our software on a Linux operation system due to a number of Linux-dependent software packages generating input features. If you have the feature files as shown in `./input/`, you are able to run our program on multiple platforms, e.g. Windows and Mac. Please be sure of python (version>3.5) installed before using. We highly recommend [Anaconda](https://www.anaconda.com/distribution/), an integrated development environment of python, which eases the use and management of python packages.

## Installation
    
1. **install dependencies**.
    * [HHblits](https://github.com/soedinglab/hh-suite) - generating multiple sequence alignments
    * [Gaussian DCA](https://github.com/carlobaldassi/GaussDCA.jl) - predictor of residue contacts
    * [Freecontact](https://rostlab.org/owiki/index.php/FreeContact) - predictor of residue contacts
    * [Phobius](http://phobius.sbc.su.se/data.html) - predictor of transmembrane topologies
2. **install protein sequence database**.    
    * [Uniclust30 database](http://gwdu111.gwdg.de/~compbiol/uniclust/2020_03/) - a curated protein sequence database based on UniProt for HHblits

3. **install DeepTMInter**

    * To download the prediction models [here](https://github.com/2003100127/deeptminter/releases). Please put the models in folder [deeptminter/model/](https://github.com/2003100127/deeptminter/tree/main/model).

    * To download a stable version of DeepTMInter [here](https://github.com/2003100127/deeptminter/releases).
    

    * To obtain the latest version of DeepTMInter do
        ```
        git clone https://github.com/2003100127/deeptminter.git
        ```
4. **install DeepTMInter of a Docker version (optional)**

    * To install Docker [here](https://www.docker.com/).

    * To download the five partitioned Docker packages [here](https://github.com/2003100127/deeptminter/releases).

    * To use [7z](https://www.7-zip.org/) to decompress the 5 partitioned Docker packages. This step will result in a file named `deeptminter_10.docker`.

    * to import `deeptminter_10.docker` by 
        ```
        docker load < deeptminter_10.docker
        ```
    
    * to use `deeptminter_10.docker` by 
        ```
        docker exec -it deeptminter_10.docker bash
        ```
    
5. **install python dependencies**
    
    ```    
	pip install -r requirements.txt
	```

## Usage

1. **`src/troll.sh`**

    * description
        troll.sh is used to generate multiple sequence alignments, transmembrane topologies, and all of evolutionary coupling features including EVfold (generated using FreeContact) and Gaussian DCA.

    * shell commands
        * general (please specify the installed location of the executables or the database in `Installations 1 and 2` and put your fasta sequence in the input path before running the following command.)
            ```
            ./troll.sh -n NAME -c CHAIN -i /YOUR/INPUT/PATH/
            ```
        * example
            ```
            ./troll.sh -n 3jcu -c H -i ./input/
            ```
    * parameters
	    * required
            ```
            -n --name -> a sequence name.
            -c --chain -> a chain name
            -i --input -> input path
            ```

2. **`src/gdca.julia`**
    
    * description
        
        `gdca.julia` is used to generate Gaussian DCA file. You'd better run it cf. https://github.com/carlobaldassi/GaussDCA.jl.
        
3. **`run_deeptminter.py`**
    
    * description
        
        If you have the feature files shown in the `./input/` directory, you can skip over steps 1-2 to step 3. We tested this step in a rigorous way. Be sure of every feature file already in the `./input/` or your preferred input file path. Finally, it works easily like this. 
    
	* python commands
	    * general
            ```python=
            python run_deeptminter.py -n NAME -c CHAIN -i /YOUR/INPUT/PATH/ -o /YOUR/OUTPUT/PATH/ -r REGION
            ```
	    * example
            ```python=
            python run_deeptminter.py -n 3jcu -c H -i ./input/ -o ./output/ -r transmembrane
            ```
	* parameters
	    * required
            ```bash=
            -n --name -> a sequence name. For example, '3jcu'.
            -c --chain -> a chain name. For example, 'H'. This can be empty if you prefer a sequnce name like '3jcuH' or '0868'.
            -i --input -> input path
            -o --output --> prediction results
            -r, --region --> region of transmembrane protein. It can take 'transmembrane', 'cytoplasmic', 'extracellular', 'combined', 'all where 'combined' means accumulation of 'transmembrane', 'cytoplasmic', 'extracellular'. 'all' means the whole fasta sequence.
            ```

2. description of output file

    It finally returns an output file with the suffix of `.deeptminter`.
    * The predictions of interaction sites in tansmembrane proteins are shown in the output file, with three columns: 1). positions of animo acids in the input sequence; 2) animo acids; 3) probabilities of being interaction sites.
    * Please **note** that if you have a sequence sharing a high sequence identity to the proteins in the [TrainData](https://data.mendeley.com/datasets/2t8kgwzp35) dataset, we recommend that any of the three output files with the suffix '.mexpand1;.mexpand2;.mexpand3' would be the best option for you.
    * If you want to get the results in the context of no ideally preferred regions predicted by Phobius. You can set `-r` as `combined` to run the program. This will return the predictions of the whole fasta sequence. Then, you can tailor the whole predictions to whatever you want.

## How to cite
J. Sun. D. Frishman. Improved sequence-based prediction of interaction sites in α-helical transmembrane proteins by deep learning. ***Comput. Struct. Biotechnol. J.***, 19:1512-1530, 2021. DOI: [10.1016/j.csbj.2021.03.005](https://doi.org/10.1016/j.csbj.2021.03.005).

or

```c
@article{DeepTMInter2021,
    title = {Improved sequence-based prediction of interaction sites in α-helical transmembrane proteins by deep learning},
    author = {Jianfeng Sun and Dmitrij Frishman},
    journal = {Computational and Structural Biotechnology Journal},
    volume = {19},
    pages = {1512-1530},
    year = {2021},
    issn = {2001-0370},
    doi = {https://doi.org/10.1016/j.csbj.2021.03.005},
    url = {https://www.sciencedirect.com/science/article/pii/S2001037021000775},
}
```

## Contact
If you have any question, please contact [Jianfeng Sun](mailto:jianfeng.sunmt@gmail.com/jianfeng.sun@tum.de). We highly recommend creating [issue](https://github.com/2003100127/deeptminter/issues) pages when you have problems. Your issues will subsequently be responded.  