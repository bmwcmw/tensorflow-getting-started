## Getting Started

### Install from Anaconda
    conda create -n tensorflow python=3.5

    activate tensorflow

    (tensorflow)C:>  # Your prompt should change 

    (tensorflow)C:> pip install --ignore-installed --upgrade tensorflow

or

    (tensorflow)C:> pip install --ignore-installed --upgrade tensorflow-gpu
    
or with requirements.txt

    conda create -n venv python=3.5

    activate venv
    
    conda install --yes --file requirements.txt

### Install from venv
    virtualenv -p python3 venv

    source venv/bin/activate
    
    pip install -r requirements.txt
    
### Run tensorboard
    python -m tensorboard.main --logdir=tb_logs

### Q&A
Proxy settings

- for pip/pip3 : add argument

     `--proxy http://proxyweb:8080`
- for python : runtime variables 

    `HTTP_PROXY=http://proxyweb:8080`
    (`HTTPS_PROXY=http://proxyweb:8080`) 

If installation package not found, specify the wheel version.
Check versions here :
https://pypi.python.org/pypi/tensorflow

    pip3 install --ignore-installed --upgrade https://pypi.python.org/packages/bf/d4/80197f48f9fb90a17c47cdd834b2f13d5f714f26e8ed5c77069d57aa3ecb/tensorflow-1.3.0-cp36-cp36m-win_amd64.whl

    pip install --ignore-installed --upgrade https://pypi.python.org/packages/bf/d4/80197f48f9fb90a17c47cdd834b2f13d5f714f26e8ed5c77069d57aa3ecb/tensorflow-1.3.0-cp36-cp36m-win_amd64.whl

If "Not valid wheel" issue, download the wheel to local and rename it to the valid py version

If "module not found", check `pip show tensorflow` and eventually install [Redistribuable Visual C++ pour Visual Studio 2015](https://www.microsoft.com/fr-FR/download/details.aspx?id=48145) that contains MSVCP140.dll etc.

If "ImportError: No module named tensorflow" : run script with right python executable/env !