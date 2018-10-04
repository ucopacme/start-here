Hands-On Labs - From Console to Code
====================================

The following is a series of self-paced lab exercises designed to introduce new
users to management of AWS resources with code.  Work on each exercise using
all of the following AWS deployment methods:

- AWS console
- AWS CLI
- CloudFormation
- boto3 SDK
- boto3 SDK with unit-test

Submit your solutions to your personal GitHub account in a repository named
``hands-on-lab-solutions``.  You do not need to submit a AWS Console solution.
We will take your word for it.  AWS CLI solutions can be shell script or a
cut-n-paste of your shell session.  For CloudFormation solutions, submit a yaml
or json template file.  For boto3 solutions, submit an executible python
script.  

For boto3 solutions we recommend you start out by using service clients_ rather
than resources_.  Clients provide a low-level interface to AWS whose methods map
close to 1:1 with AWS CLI.

See the ``hands_on_lab/sample_solutions`` directory for a complete example.


Lab 1 - IAM User
----------------

- Create an IAM user and group  
- Add the user to the group
- Delete both user and group


Lab 2 - S3 Bucket
-----------------

- Create an S3 bucket
- Add an object to the bucket
- Delete both object and bucket


Lab 3 - EC2 Instance
--------------------

- Create an EC2 instance in the default VPC
- Supply your public ssh key
- Launch your instance
- Log into your instance with ssh
- Delete your instance







.. _client: https://boto3.amazonaws.com/v1/documentation/api/latest/guide/clients.html
.. _resource: https://boto3.amazonaws.com/v1/documentation/api/latest/guide/resources.html#overview
