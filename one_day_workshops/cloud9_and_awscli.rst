Cloud9 and AWS CLI
==================

Goals

- understand AWS cloud9 service
- get started with AWS CLI

Prerequisites:

- AWS login profile and credentials for the Auth account
- ability to assume role into the training account
- either Chrome or Firefox

Required params:

- Auth account login URL
- account alias of the training account
- role name to use for switching roles into the training account


Working with Cloud9
-------------------

We will basically be following the instructions for steps 1 and 2 of the AWS
Cloud9 tutorial
https://docs.aws.amazon.com/cloud9/latest/user-guide/tutorial.html

**Get to Cloud9 Service Page**

- log into the AWS console with your Auth account credentials
- assume role into the training account
- click on **Services** tab
- type in ``cloud9`` and press ``<Enter>``

Spend some time reading the info on this page.  Notice the various links to 
documentation and resources.

**Create your instance**

**NOTE**
  Cloud9 does not support Internet Explorer.  Please use either Chrome
  or Firefox.

- validate you are in the ``Oregon/us-west-2`` region
- press **Create Environment**
- put your IAM user name in **Name** field
- for all other options you can just use defaults
- click your way through the dialogues to create the environment


**Explore the Cloud9 IDE**

Follow Step 2 of the section of the Cloud9 tutorial.  This provides a thorough
tour of the cloud9 IDE, much better than I could write:
https://docs.aws.amazon.com/cloud9/latest/user-guide/tutorial.html#tutorial-tour-ide


Intro to AWS CLI
----------------

**Getting help with AWS CLI**

In your cloud9 instance open a terminal.  Welcome to the Linux command line.

Cloud9 instances come with the awscli python package pre-installed.  Have a 
look at the aws cli help system.  Run::

  aws help
  aws s3api help
  aws s3api create-bucket
  aws ec2 help
  aws ec2 create-instance help


In addition the full command reference is available online:
https://docs.aws.amazon.com/cli/latest/reference/

From the **Table of Contents** on the left select **Available Services**.  Pick
one of these and drill into some of the commands.


**Configure tab completion**

As with any well written Unix command, awscli supports tab completion.
Run the following commands in your terminal session::

  echo "source /etc/bash_completion.d/aws_bash_completer" >> ~/.bashrc
  source ~/.bashrc


**AWS CLI User Guide**

AWS provides excellent documentation for all services and tools.  For 
AWS CLI visit the user guide: https://docs.aws.amazon.com/cli/latest/userguide/cli-chap-welcome.html

For now we skip ahead to the section on *Using the Command Line Interface*:
https://docs.aws.amazon.com/cli/latest/userguide/cli-chap-using.html

Read through the following sections.  This will help immeasurably with 
the exercises below:

- Command Structure
- Specifying Parameter Values
- Generate CLI Skeleton
- Controlling Command Output
- Shorthand Syntax


**Working with S3**

By now you should be ready to try out some aws cli commands from your cloud9
terminal session.  Using the ``s3api`` service and the help menus to guide you,
perform the following:

- list all s3 buckets
- create a new bucket with name ``<USER>-one-day-workshop``, where ''<USER>''
  is your IAM user name you used to log into the Auth account.
- put an object in your bucket
- list objects in your bucket
- delete all bucket objects
- delete your bucket

You will be using a combination of the ``s3api`` sub-commands listed below.  

- create-bucket
- list-buckets
- list-objects
- delete-object
- delete-bucket
- put-object

NOTE: You will need to specify a location constraint when running
``create-bucket``. (hint: ``--region us-east-1``)

Make use of google.  There are lots of examples out there.  I only ask that you
do not cut-and-paste, but type out all commands.  Make use of tab completion.

For more info on working with S3 see the *S3 Developer Guide*:
https://docs.aws.amazon.com/AmazonS3/latest/dev/Welcome.html




**Working with EC2**

AWS provides a good tutorial for creating an ec2 instance with AWS CLI:
https://docs.aws.amazon.com/cli/latest/userguide/tutorial-ec2-ubuntu.html

Since you are in Cloud9, you do not need to configure your access keys.  Skip
to the section *Create a Security Group and Key Pair for the EC2 Instance*
and follow the rest of the tutorial.

Again, I recommend you avoid cut-and-paste and type out the command lines.
Make use of tag completion.

