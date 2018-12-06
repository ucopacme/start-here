Cloud9 and AWS CLI
==================

Goals

- understand AWS cloud9 service
- get started with AWS CLI

Prerequisites:

- AWS login profile and credentials for the Auth account
- ability to assume role into the training account


Working with Cloud9
-------------------

We will basically be following the instructions for steps 1 and 2 of the AWS
Cloud9 tutorial
https://docs.aws.amazon.com/cloud9/latest/user-guide/tutorial.html

**Get to Cloud9 Service Page**

- log into the AWS console: https://seg-auth.signin.aws.amazon.com/console
- assume role into the training account
- click on **Services** tab
- type in `cloud9` and press `<Enter>`

Spend some time reading the info on this page.  Notice the various links to 
documentation and resources.

**Create your instance**

- validate you are in the `Origon/us-west-2` region
- press **Create Environment**
- put your IAM user name in **Name** field
- for all other options you can just use defaults
- click your way through the dialogs to create the environment


**Explore the Cloud9 IDE**

Follow Step 2 of the section of the Cloud9 tutorial.  Thisprovides a thorogh
tour of the cloud9 IDE, much better than I could write:
https://docs.aws.amazon.com/cloud9/latest/user-guide/tutorial.html#tutorial-tour-ide


Intro to AWS CLI
----------------

**Getting help with AWS CLI**

In your cloud9 instance open a terminal.  Welcome to the linux command line.

Cloud9 instances come with the awscli python package pre-installed.  Have a 
look at the aws cli help system.  Run::

  aws help
  aws s3api help
  aws s3api create-bucket
  aws ec2 help
  aws ec2 create-instance help


In addition the full command reference is available online:
https://docs.aws.amazon.com/cli/latest/reference/

On the Table of contents on the left select `Available Services`.  Pick
one of these and drill into some of the commands.


**AWS CLI User Guide**

AWS provides excellent documentation for all services and tools.  For 
AWS CLI visit the user guide: https://docs.aws.amazon.com/cli/latest/userguide/cli-chap-welcome.html

For now we skip ahead to the section on *Using the Command Line Interface*:
https://docs.aws.amazon.com/cli/latest/userguide/cli-chap-using.html

Read through the following sections.  This will help immeasurabley with 
the excercises below:

- Command Structure
- Specifying Parameter Values
- Generate CLI Skeleton
- Controlling Command Output
- Shorthand Syntax


**Working with S3**

By now you should be ready to try out some aws cli commands from your cloud9
terminal session.  Using the `s3api` service and the help menus to guide you,
perform the following:

- list all s3 buckets
- create a new bucket with name $USER-one-day-workshop, where $USER is your
  IAM user name you used to log in to the Auth account.

- put an object in your bucket
- list objects in your bucket
- delete all bucket objects
- delete your bucket

You will be using a combination of the `s3api` subcommands listed below.  

- create-bucket
- list-buckets
- list-objects
- delete-object
- delete-bucket
- put-object

NOTE: You will need to specify a location constraint when running
`create-bucket`. (hint: `--region us-east-1`)

Make use of google.  There are lots of examples out there.  I only ask that you
do not cut and paste, but type out all commands.  

For more info on working with S3 see the *S3 Developer Guide*:
https://docs.aws.amazon.com/AmazonS3/latest/dev/Welcome.html




**Working with EC2**


