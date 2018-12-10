Linux Workstation Setup
=======================

Goals

- Python3 virtual environment
- AWS CLI environment
- UCOP aws-shelltools in Linux 

Prerequisites

- Linux Platform (CentOS, AWS Cloud9)
- LInux user account, bash environment
- AWS service access through anagement console 
- AWS IAM service access to retrieve security credential


Python3 Package
---------------

From bash command prompt::

  # Check Python3.x package installation
  $ python3 -V

  # Install Python3.x package
  $ cd ~/Download
  $ wget https://www.python.org/ftp/python/3.6.4/Python-3.6.4.tgz
  $ tar zxvf ./Python-3.6.4.tgz
  $ cd Python-3.6.4
  $ configure
  $ make
  $ sudo make install
  $ python3 -V

  # Install PIP Python Installation Package
  $ cd ~/Download
  $ curl -O https://bootstrap.pypa.io/get-pip.py
  $ sudo python   get-pip.py
  $ pip install --upgrade pip

  
Python3 Virtual Environment
---------------------------

From bash command prompt::

  # Create python3 virtual environment
  $ mkdir ~/python
  $ python3 -m venv ~/python/py36

  # Add following bash alias in .bashrc
  $ alias py36='source ~/python/py36/bin/activate'

  # Working from python3 virtual environment
  $ cd 
  $ py36
  (py36) $ python3 -V
  (py36) $ pip install --upgrade pip


AWS CLI installation 
--------------------

Install AWS CLI within python3 virtual environment::

  # Install AWS CLI
  (py36) $ pip3 install awscli
  (py36) $ aws --version

  # add following AWS CLI command completer in .bashrc 
  (py36) $ complete -C '/home/jhsu/python/py36/bin/aws_completer' aws
  (py36) $ . ~/.bashrc

AWS configuration
-----------------

Create AWS access key from AWS IAM console and run following command::

  # aws configure 
  (py36) $ aws configure
  AWS Access Key ID [None]:
  AWS Secret Access Key [None]:
  Default region name [None]: us-west-2
  Default output format [None]:

  # check AWS credentials in ~/.aws directory
  (py36) $ cd ~/.aws
  (py36) $ cat config
  (py36) $ cat credentials


aws-shelltools and AWS STS service
----------------------------------

Install aws-shell-tools within python3 virtual environment::

  # pip install aws-shelltools
  (py36) $ cd  
  (py36) $ pip install https://github.com/ucopacme/aws-shelltools/archive/master.zip 
  
  # source ~/.bashrc 
  (py36) $ . ~/.bashrc

  # run aws-shelltools script functions from bash prompt 

  # Print current values of all AWS environment vars
  (py36) $ aws-env

  # Print output of 'aws sts get-caller-identity'
  (py36) $ aws-whoami

  # Request temporary session credentials from AWS STS
  (py36) $ aws-set-mfa-token

  # Print current values of all AWS environment vars
  (py36) $ aws-env

  # Print output of 'aws sts get-caller-identity'
  (py36) $ aws-whoami

  # Print current values of AWS assumed role environment vars
  (py36) $ aws-display-assumed-role

  # Print list of available AWS assume role profiles
  (py36) $ aws-list-roles

  # Run 'aws sts assume-role' operation to obtain temporary assumed role credentials
  (py36) $ aws-assume-role ait-training-xxxx

  # Print current values of AWS assumed role environment vars
  (py36) $ aws-display-assumed-role

  # Print current values of all AWS environment vars
  (py36) $ aws-env

  # Print output of 'aws sts get-caller-identity'
  (py36) $ aws-whoami

  # Unset all AWS session token environemt vars
  (py36) $ aws-unset-mfa-token

  # Reset AWS session environment vars to values prior to assuming role
  (py36) $ aws-drop-assumed-role

  # Print current values of AWS assumed role environment vars
  (py36) $ aws-display-assumed-role

  # Print output of 'aws sts get-caller-identity'
  (py36) $ aws-whoami

  # Print current values of all AWS environment vars
  (py36) $ aws-env

  # Refer to following documents for aws-shelltools pacakge
  https://github.com/ucopacme/aws-shelltools






   


