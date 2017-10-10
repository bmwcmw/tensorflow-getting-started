## Getting Started

### Install from Anaconda

`conda create -n tensorflow python=3.5`

`activate tensorflow`

(tensorflow)C:>  # Your prompt should change 

`(tensorflow)C:> pip install --ignore-installed --upgrade tensorflow`

or
`(tensorflow)C:> pip install --ignore-installed --upgrade tensorflow-gpu`

### Install from Native (>= 3.3)

`pip install --ignore-installed --upgrade tensorflow`
or
`pip install --ignore-installed --upgrade tensorflow-gpu`

### Install additional libs
`pip3 install --proxy http://proxyweb:8080 matplotlib`

### Q.

If installation package not found, specify the wheel version.
Check versions here :
https://pypi.python.org/pypi/tensorflow

`pip3 install --ignore-installed --upgrade https://pypi.python.org/packages/bf/d4/80197f48f9fb90a17c47cdd834b2f13d5f714f26e8ed5c77069d57aa3ecb/tensorflow-1.3.0-cp36-cp36m-win_amd64.whl --proxy http://proxyweb:8080`

`pip install --ignore-installed --upgrade https://pypi.python.org/packages/bf/d4/80197f48f9fb90a17c47cdd834b2f13d5f714f26e8ed5c77069d57aa3ecb/tensorflow-1.3.0-cp36-cp36m-win_amd64.whl --proxy http://proxyweb:8080`

If "Not valid wheel" issue, download the wheel to local and rename it to the valid py version

If "module not found", check `pip show tensorflow` and eventually install [Redistribuable Visual C++ pour Visual Studio 2015](https://www.microsoft.com/fr-FR/download/details.aspx?id=48145) that contains 