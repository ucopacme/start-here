Hands-On Labs - From Console to Code
====================================

The following is a series of self-paced lab exercises designed to introduce new
users to management of AWS resources with code.  Work on each exercise using
all of the following AWS deployment methods:

- AWS console
- AWSCLI_
- CloudFormation_
- `Boto3 SDK`_
- `Boto3/Moto Unit Testing`_


To post your solutions follow the `Contributing to Github`_ workflow.  Make a
fork of this repository in your personal GitHub account.  Add a directory for
yourself under ``hands_on_lab/user_solutions/`` and post your code within
subdirs named for each lab::

  mkdir -p hands_on_lab/user_solutions/$USER/lab1
  cp ~/lab1_code/* hands_on_lab/user_solutions/$USER/lab1

You do not need to submit a AWS Console solution.  We will take your word for
it.  AWS CLI solutions can be shell script or a cut-n-paste of your shell
session.  For CloudFormation solutions, submit a yaml or json template file
along with a script containing launch/delete instructions.  For boto3 and
unit-test solutions, submit an executable python script with usage examples.  

See `sample solutions`_ for a complete example.


Peer Review
-----------

Once you have completed all five parts of a lab, open an issue and pull request in this
github repo to review your solutions: ``[Resolves #<issue_number>] peer review ashley's lab1 solutions``

Peer review will include the following:

- are all five deployment methods complete?
- do all code solutions run without error?
- do unit-tests pass?
- do solutions demonstrate understanding of the various deployment methods?
- are code solutions well organized and well formatted?


Level 1
-------


Lab 1 - S3 Bucket
*****************

- Create an S3 bucket
- Validate bucket creation
- Delete bucket


Lab 2 - IAM User
****************

- Create an IAM user
- Validate user creation
- Delete user


Lab 3 - EC2 Instance
********************

- Launch EC2 instance in the default VPC
- Validate instance is running
- Delete instance


Level 2 - Builds off of Level 1 solutions
-----------------------------------------


Lab 4 - S3 Object in Bucket
***************************

- Create an S3 bucket
- Add an object to the bucket
- Validate bucket is in object
- Delete both object and bucket


Lab 5 - IAM User in Group
*************************

- Create IAM user
- Create IAM Group
- Add the user to the group
- Validate user is in group
- Delete both user and group


Lab 6 - SSH to EC2 Instance
***************************

- Create or upload an SSH keypair into EC2 service
- Create a EC2 SecurityGroup in default VPC with rule allowing ssh access
- Launch an EC2 instance your SSH keypair and SecurityGroup as properties
- Log into your instance with ssh
- Delete your EC2 instance, SSH keypair and SecurityGroup



Prerequisites
-------------

- Create a `github account`_
- Set up `python 3 virtual environnment`_
- Install and configure awscli_
- Install and configure aws-shelltools_


Reference Documentation
-----------------------

AWSCLI
******

- https://docs.aws.amazon.com/cli/latest/userguide/cli-chap-using.html
- https://docs.aws.amazon.com/cli/latest/reference/
- https://docs.aws.amazon.com/cli/latest/reference/s3api/index.html

CloudFormation
**************

- https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/GettingStarted.html
- https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/template-anatomy.html
- https://docs.aws.amazon.com/cli/latest/reference/cloudformation/index.html
- https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-s3-bucket.html
- https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/sample-templates-services-us-west-2.html

Boto3 SDK
*********

For boto3 solutions we recommend you start out by using service clients_ rather
than resources_.  Clients provide a low-level interface to AWS whose methods map
close to 1:1 with AWS CLI.

- https://boto3.amazonaws.com/v1/documentation/api/latest/index.html
- https://boto3.amazonaws.com/v1/documentation/api/latest/guide/s3-example-creating-buckets.html
- https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3.html#client

Boto3/Moto Unit Testing
***********************

We recommend starting with pytest and moto for your unit-test labs.

- https://docs.pytest.org/en/latest/contents.html#toc
- https://semaphoreci.com/community/tutorials/testing-python-applications-with-pytest
- https://github.com/spulec/moto
- http://docs.getmoto.org/en/latest/docs/getting_started.html


.. _Contributing to Github: https://github.com/ucopacme/start-here/blob/master/docs/contributing.rst
.. _sample solutions: https://github.com/ucopacme/start-here/tree/master/hands_on_lab/sample_solutions
.. _clients: https://boto3.amazonaws.com/v1/documentation/api/latest/guide/clients.html
.. _resources: https://boto3.amazonaws.com/v1/documentation/api/latest/guide/resources.html#overview
.. _github account: https://github.com/
.. _python 3 virtual environnment: https://github.com/ucopacme/start-here/blob/master/docs/python_venv_setup.rst
.. _awscli: https://docs.aws.amazon.com/cli/latest/userguide/installing.html
.. _aws-shelltools: https://github.com/ashleygould/aws-shelltools
