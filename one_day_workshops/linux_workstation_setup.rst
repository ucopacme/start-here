Linux Workstation Setup
=======================

Goals

- Create Python3 virtual environment
- AWS CLI environment
- Install UCOP aws-shelltools package 

Prerequisites

- Linux Platform (CentOS, AWS Cloud9)
- Linux user account, bash environment
- AWS service access through management console 
- AWS IAM service access to retrieve security credential

Reference
- Refer to following documents for aws-shelltools pacakge
- https://github.com/ucopacme/aws-shelltools


Cloud9 Setup
------------

If you are working from a cloud9 environment you should create a local
user and do the workshop as that user::

As ec2-user
  
  $ sudo useradd -m localuser
  $ sudo su - localuser

As localuser
  
  $ echo "source /etc/bash_completion.d/aws_bash_completer" >> ~/.bashrc
  $ source ~/.bashrc


Python3 Package
---------------

From bash command prompt::

  Check Python3.x package installation
  
  $ python3 -V

  Install Python3.x package
  
  $ cd ~/Download
  $ wget https://www.python.org/ftp/python/3.6.4/Python-3.6.4.tgz
  $ tar zxvf ./Python-3.6.4.tgz
  $ cd Python-3.6.4
  $ configure
  $ make
  $ sudo make install
  $ python3 -V

  Install PIP Python Installation Package
  
  $ cd ~/Download
  $ curl -O https://bootstrap.pypa.io/get-pip.py
  $ sudo python   get-pip.py
  $ pip install --upgrade pip

  
Python3 Virtual Environment
---------------------------

From bash command prompt::

  To avoid python version conflicts with other pip packages, 
  create python3 virtual environment

  $ mkdir ~/python
  $ python3 -m venv ~/python/py36

  Add following bash alias in .bashrc

  alias py36='source ~/python/py36/bin/activate'

  Entering python3 virtual environment

  $ cd
  $ py36
  (py36) $ python3 -V
  (py36) $ pip install --upgrade pip
 

AWS CLI installation 
--------------------

Install AWS CLI within python3 virtual environment::

  Install AWS CLI
  
  (py36) $ pip install awscli
  (py36) $ aws --version

   Add following AWS CLI command completer in .bashrc 
  
  (py36) $ complete -C '/home/jhsu/python/py36/bin/aws_completer' aws
  (py36) $ . ~/.bashrc

AWS configuration
-----------------

Create AWS access key from AWS IAM console and run following command::

  For general use, the aws configure command is the fastest way 
  to set up your AWS CLI installation.
  Supply AWS account credential generated from IAM user service 
  when running 'aws configure'
  Refer to https://docs.aws.amazon.com/cli/latest/userguide/cli-chap-configure.html
  
  Access keys consist of an access key ID and secret access key, 
  which are used to sign programmatic requests that you make to AWS.

  From AWS IAM console, switch back to seg-auth account.
  Access the IAM service, and re-generate security credential.

  (py36) $ aws configure
  AWS Access Key ID [None]: AKI**********W5AFPSNQ
  AWS Secret Access Key [None]: U/QotA**********************543vuYB
  Default region name [None]: us-west-2
  Default output format [None]:

  The AWS CLI supports named profiles stored in the config and 
  credentials files. 
  You can configure additional profiles by using aws configure 
  with the --profile option or by adding entries to the config 
  and credentials files.
  
  check AWS default profile in ~/.aws directory
  
  (py36) $ cd ~/.aws
  (py36) $ cat config
  (py36) $ cat credentials


aws-shelltools and AWS STS service
----------------------------------

Install aws-shelltools within python3 virtual environment::

  # Install aws-shelltools package
  #
  (py36) $ cd  
  (py36) $ pip install https://github.com/ucopacme/aws-shelltools/archive/master.zip 
  (py36) $ pip list | grep aws-shelltools
  
  # Run aws-shelltool-setup
  # and source ~/.bashrc
  #
  (py36) $ which aws-shelltools-setup
  (py36) $ aws-shelltools-setup
  (py36) $ . ~/.bashrc

  # Generate aws client configuation file
  # 
  (py36) $ cd
  (py36) $ aws-make-config

  # List of porfile to be assumed
  #
  (py36) $ cd ~/.aws/config.d
  (py36) $ ls config.aws_shelltools

  # Following is the list of defined bash function from aws-shelltools python package
  #
  # aws-whoami()
  # aws-env()
  # aws-unset-mfa-token()
  # aws-display-assumed-role()
  # aws-drop-assumed-role()
  # aws-profile()
  # aws-set-mfa-token()
  # aws-list-roles()
  # aws-assume-role()
  # aws-refresh()
  # aws-list-roles()
  # aws-export-env()
  # aws-import-env()
  #
  (py36) $ aws-env
  (py36) $ aws-whoami

  The AWS CLI supports the following environment variables.

  AWS_ACCESS_KEY_ID – AWS access key.
  
  AWS_SECRET_ACCESS_KEY – AWS secret key. Access and secret key variables 
  override credentials stored in credential and config files.
  
  AWS_SESSION_TOKEN – Specify a session token if you are using 
  temporary security credentials.
  
  AWS_DEFAULT_REGION – AWS region. This variable overrides 
  the default region of the in-use profile, if set.
  
  AWS_DEFAULT_OUTPUT – Change the AWS CLI's output formatting 
  to json, text, or table.
  
  AWS_PROFILE – name of the CLI profile to use. This can be 
  the name of a profile stored in a credential or config file, 
  or default to use the default profile.
  
  AWS_CA_BUNDLE – Specify the path to a certificate bundle 
  to use for HTTPS certificate validation.
  
  AWS_SHARED_CREDENTIALS_FILE – Change the location of the file 
  that the AWS CLI uses to store access keys.
  
  AWS_CONFIG_FILE – Change the location of the file that 
  the AWS CLI uses to store configuration profiles.


  # run aws-shelltools script functions from bash prompt 

  # Print current values of all AWS environment vars
  #
  (py36) $ aws-env

  # Print output of 'aws sts get-caller-identity'
  #
  (py36) $ aws-whoami

  # Request temporary session credentials from AWS STS
  #
  (py36) $ aws-set-mfa-token

  # Print current values of all AWS environment vars
  #
  (py36) $ aws-env

  # Print output of 'aws sts get-caller-identity'
  #
  (py36) $ aws-whoami

  # Print current values of AWS assumed role environment vars
  #
  (py36) $ aws-display-assumed-role

  # Print list of available AWS assume role profiles
  #
  (py36) $ aws-list-roles

  # Run 'aws sts assume-role' operation to obtain temporary assumed role credentials
  #
  (py36) $ aws-assume-role ait-training-xxxx

  # Print current values of AWS assumed role environment vars
  #
  (py36) $ aws-display-assumed-role

  # Print current values of all AWS environment vars
  #
  (py36) $ aws-env

  # Print output of 'aws sts get-caller-identity'
  #
  (py36) $ aws-whoami

  # Unset all AWS session token environemt vars
  #
  (py36) $ aws-unset-mfa-token

  # Reset AWS session environment vars to values prior to assuming role
  #
  (py36) $ aws-drop-assumed-role

  # Print current values of AWS assumed role environment vars
  #
  (py36) $ aws-display-assumed-role

  # Print output of 'aws sts get-caller-identity'
  #
  (py36) $ aws-whoami

  # Print current values of all AWS environment vars
  #
  (py36) $ aws-env







   


