Python36 Virtual Environment
============================


Install python from source
----------------------------

Here is a recipe for building python 3.6.4 on Fedora 25.  Be sure to include 
readline development libs.  This permits tab completion in interactive mode::

  sudo dnf install -y gcc make zlib-devel bzip2 bzip2-devel readline-devel sqlite sqlite-devel openssl-devel xz xz-devel
  mkdir -p downloads/tgz
  cd downloads/tgz
  wget https://www.python.org/ftp/python/3.6.4/Python-3.6.4.tgz
  mkdir ~/build
  cd ~/build/
  tar zxvf ~/downloads/tgz/Python-3.6.4.tgz
  cd Python-3.6.4/
  ./configure && make && sudo make install
  which python3


Create python venv
------------------

Setup your venv:: 

  mkdir ~/python
  python3 -m venv ~/python/python36

Activate (deactivate) your venv for this shell session::

  source ~/python/python36/bin/activate
  deactivate

Add this to your ~/.bashrc or ~/.aliases::

  alias py3='source ~/python/python36/bin/activate'

Installing python packages into your venv::

  py3
  pip install -U pip
  pip install awscli boto3


On-Line Tutorial
----------------

intro to virtual environments

https://www.youtube.com/watch?v=N5vscPTWKOk



