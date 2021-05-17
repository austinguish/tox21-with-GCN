# GCN on tox21
## Intro
Use GCN to extract the compounds's features,predict whether they could activate the signal path.
## install
Conda environment is recommended.
use folowing command to set a conda virtual env.

`$conda create --name DGL_py36_pytorch1.2_chem`

`$conda install --name DGL_py36_pytorch1.2_chem pytorch=1.2 torchvision -c pytorch`

`$conda install --name DGL_py36_pytorch1.2_chem -c dglteam dgl-cuda10.0=0.4.0`

`$conda install --name DGL_py36_pytorch1.2_chem --update-deps --force libpng`

`$conda install --name DGL_py36_pytorch1.2_chem --update-deps --force -c conda-forge rdkit`
## run
`$conda activate DGL_py36_pytorch1.2_chem`

`$python test.py`

