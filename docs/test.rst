VM Import/Export Solution Migration
===================================

**Context:**
 Facilitating the Import of a Virtual Machines into AWS as a way to satisfy multiple requirements such as migrations of smalle
 r scoped environments,  ensure Disaster Recovery and/or Backups of system or application data is captured.


**Goals:**
 This initial draft seeks to discover different methos of moving Virtual Machines or application data from an On-Premise farm
 to aand AWS account.

What is VM Import/Export:
-------------------------
- VM Import/Export enables you to import virtual machine (VM) images from your existing virtualization environment to Amazon EC2, and then export them back.


What functionality is provided:
-------------------------------
- The ability to import a VM from your virtualization environment to Amazon EC2 as an Amazon Machine Image (AMI). You can launch EC2 instances from your AMI any time.



Types of VM Import/Export:
--------------------------
- Image import  ( supports Multi-disk imports and Windows BYOL)
- Instance import ( Multi-disk imports and Windows BYOL)
- Snapshot Import ( Import a VMDK and create and EBS volume than attach to an EC2 Instance)

**Walk-thru** of utilizing VM Import/Export - Image Version:
--------------------------------------------

- On our On-Premise VMWare farm - create an OVA based off the VMWare Virtual Machine required to be migrated. *(refer to Vsphere documentations on creating the proper export data)*

Create an S3 Bucket within the region you wish to store your VM data.
::
    aws s3 mb s3://ait-migrate-aws

Copy the OVA to an S3 Bucket
::
    aws s3 cp scrappy-clone.ova s3://ait-migrate-aws

Create a trust Policy - which trusted account members are allowed to assume the role.
::
    vi trust-policy.json
       {
   "Version": "2012-10-17",
   "Statement": [
      {
         "Effect": "Allow",
         "Principal": { "Service": "vmie.amazonaws.com" },
         "Action": "sts:AssumeRole",
         "Condition": {
            "StringEquals":{
               "sts:Externalid": "vmimport"
            }
         }
      }
   ]
}

Create an IAM Role utilizing the trust policy
::
   aws iam create-role --role-name vmimport --assume-role-policy-document file://trust-policy.json

Create a Role Policy
::

    vi  role-policy.json


        {
   "Version": "2012-10-17",
   "Statement": [
      {
         "Effect": "Allow",
         "Action": [
            "s3:ListBucket",
            "s3:GetBucketLocation",
            "s3:FullAccess"
         ],
         "Resource": [
            "arn:aws:s3:::ait-migrate-aws"
         ]
      },
      {
         "Effect": "Allow",
         "Action": [
            "s3:GetObject"
         ],
         "Resource": [
            "arn:aws:s3:::ait-migrate-aws/*"
         ]
      },
      {
         "Effect": "Allow",
         "Action":[
            "ec2:ModifySnapshotAttribute",
            "ec2:CopySnapshot",
            "ec2:RegisterImage",
            "ec2:Describe*",
            "ec2:FullAccess"
         ],
         "Resource": "*"
      }
   ]
}


Update Inline IAM Policy to use the new **role-policy.json** file
::
   aws iam put-role-policy --role-name vmimport --policy-name vmimport --policy-document file://role-policy.json

Create a **containers-json** file that will  be used to define:

- Format of VM to be imported into AWS
- S3 Bucket Location
- Virtual Machine (key)


::

    vi containers-scrappy.json

    [
       {
         "Description": "migrate from SDSC to AWS",
         "Format": "ova",
         "UserBucket": {
             "S3Bucket": "ait-migrate-aws",
             "S3Key": "scrappy-clone1.ova"
         }
     }]

Copy the **containers-json** file to the S3 Bucket utilized as a staging point for the VM inports
::
   aws s3 cp container-scrappy.json s3://ait-migrate-aws

With the VMWare image located in the S3 bucket, initiate the import:
::
   aws ec2 import-image --description "Scrappy-Clone OVA"  --disk-containers file://container-scrappy.json

List the state of the Import using the  'import-ami-###'
::
   aws ec2 describe-import-image-tasks --import-task-ids import-ami-08d161af9f9ede8aa

**OPTIONAL** - Cancelling the import task:
::
   aws ec2 cancel-import-task --import-task-id import-ami-08d161af9f9ede8aa

      -----------  AMI COMPLETED ---------
