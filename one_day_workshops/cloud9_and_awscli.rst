Cloud9 and AWS CLI
==================

Goals

- understand AWS cloud9 service
- get started with AWS CLI

Prerequisites:

- AWS login profile and credentials for the Auth account
- ability to assume role into the training account


Create a Cloud9 Instance
------------------------

We will basically be following the instructions for steps 1 and 2 of the AWS
Cloud9 tutorial
https://docs.aws.amazon.com/cloud9/latest/user-guide/tutorial.html

here is a quickstart guide for Step 1:

- log into the AWS console: https://seg-auth.signin.aws.amazon.com/console
- assume role into the training account
- click on **Services** tab
- type in `cloud9` and press `<Enter>`




- validate you are in the `Origon/us-west-2` region
- press **Create Environment**
- put your IAM user name in **Name** field
- for all other options you can just use defaults
- click your way through the dialogs to create the environment


Explore the Cloud9 IDE
----------------------

Follow Step 2 of the section of the Cloud9 tutorial.  Thisprovides a thorogh
tour of the cloud9 IDE, much better than I could write:
https://docs.aws.amazon.com/cloud9/latest/user-guide/tutorial.html#tutorial-tour-ide





Navigate to the Cloud9 Service

**cloud9 instance**

- cloud9 getting started docs
- create cloud9 instance
- explore IDE
- open terminal
- run aws cli help commands


