One-Day-Workshops Corriculum
============================

Learning to develop AWS infrastructure as code.


Day X - Console Access
----------------------

**obtain access to AWS**

- specify POC account
- specify access privilages
- login profile email

  - user configuration instructions
  - temporary credentials
  - assume role delegations listing

**first time login**

- list users
- list groups
- list policies
- reset password
- set up MFA device
- log out and log in again
- assume role into POC account

**working with S3**

- list buckets
- create bucket
- upload object
- list objects
- download object
- delete object
- delete bucket

**working with EC2**

- list instances
- create ssh keypair
- create instance
- log into instance
- delete instance

**working with IAM**

- create user
- create loginprofile
- log in as user from second browser instance

  - list s3 buckets (fails)

- create group
- attach policy to group

  - AmazonS3FullAccess
  - view policy statement

- add user to group
- log in as user from second browser instance

  - list buckets

- cleanup

  - remove user froup group
  - detach policy from group
  - delete group, user



Day X - Cloud9 and AWS CLI
--------------------------

**cloud9 instance**

- login to console and assume role into POC account
- cloud9 getting started docs
- create cloud9 instance
- explore IDE
- open terminal
- run aws cli help commands

**working with S3 in awscli**

- using `s3`

  - get help
  - list buckets
  - create bucket
  - upload object
  - list objects
  - download object
  - delete object
  - delete bucket

- using `s3api`

  - get help
  - list buckets
  - create bucket
  - upload object
  - list objects
  - download object

**working with EC2 in awscli**

- get help
- describe instances
- edit shell script in IDE to create ec2 instance

  - AMI for amazon linux
  - ssh keypair
  - userdata
  
    - run os update
  
  - instance profile
  
    - read access to s3

- create instance by running shell script
- log into instance
- check for updates
- run s3 commands with awscli

  - list buckets
  - list objects in bucket
  - download object
  - create bucket (fails)

- stop instance



Day X - Linux Workstation Setup
-------------------------------

Ideally this workshop can be performed from a cloud9 instance, but
let's assume a real linux VM running RHEL6

**python virtual environment**

- install python 3
- create python venv
- setup shell alias
- pip install awscli

**IAM access keys**

- create keys in console
- run aws configure
- review files in ~/.aws
- run aws sts get-caller-identity
- what is your ``default profile``?

**aws-shelltools**


**STS assume role deepdive**

- determine account id and access-role name for POC account
- set sts MFA tokens from cli
- run sts assume-role to access POC account
- run aws sts get-caller-identity
- set shell env vars
- create assume role profile 'training' in .aws/config for access to POC acount
- assume role syntax simplified
- aws-shelltools revisited


Day X - Cloudformation
----------------------

**cloudformation basics**

- where to find help
- managing cfn stacks in the console
- managing cfn stacks with awscli
- template anatomy
- json vs. yaml

  - pip install cfn-flip


**S3 bucket with cloudformation**

**EC2 instance with cloudformation**


Day X - Learning Git
--------------------

**git basics**

- 
- create a local repository
- commit your cloudformation templates
- create a tag
- create a topic branch and commit some changes
- merge your topic branch into master
- create another tag to update version


**working with remotes**

**codecommit**

- credential helper
- create a codecommit repository
- make this a remote to your local repo
- push to codecommit remote

**github**

- create a github account
- create a repository in your github account
- make this a remote to your local repo
- push to github remote


Day X - Boto3 Python SDK
------------------------

**getting started with boto3**

**S3 bucket with boto3**

**EC2 instance with boto3**


Day X - Unit Testing
--------------------

**python assert statement**

**pytest**

**moto**

**unit test s3bucket.py**

**unit test ec2instance.py**


Day X - Making a Python Package
-------------------------------

**directory layout**

**setup.py**

**README.rst**

- Intro to ReSTructuredText

**version your package**

**install your package with pip**

**distribute your package with PyPi**


Day X - Collaborating on Github
-------------------------------

for this we create an alternate github org for training: ucop_one_day_workshops

- create a project reposistory in ucop_one_day_workshops
- fork this project in your own github account
- create an issue in ucop_one_day_workshops
- work issue locally in a topic branch
- push topic branch to your fork
- create a pull request
- review the pull request
- merge the pull request
- close the issue
  - auto-closing issues


Day X - Automated Unit Testing
------------------------------

**pytest again**

**flake8**

**travis.ci**


Day X - Automated Project Documentation
---------------------------------------

**ReSTructuredText revisited**

**sphinx**

**Readthedocs.io**


Day X - Automated Package Deployment
------------------------------------


Day X - IAM Deep Dive
---------------------

**policy attached to group**
- create user
- create loginprofile
- create group

- create policy
  
  - allow access to s3 bucket by group
  - resource ARN
  - policy statement structure

    - effect
    - action
    - resource
    - principle

- attach policy to group
- log in as user from second browser instance

  - access bucket

- cleanup

  - remove user froup group
  - detach policy from group
  - delete group, user, policy, s3 bucket


