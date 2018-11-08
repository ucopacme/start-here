VM Import/Export Solution Migration
===================================

**Context:**
 Facilitating the Import of a Virtual Machines into AWS as a way to satisfy multiple requirements such as migrations of smaller scoped environments,  ensure Disaster Recovery and/or Backups of system or application data is captured.


**Goals:**
 This initial draft seeks to discover different methos of moving Virtual Machines or application data from an On-Premise farm to aand AWS account.

   


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

    vi 	role-policy.json


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

Creating EC2 Instance based off your **imported AMI**
::
  aws ec2 run-instances --image-id ami-06bf5a1f3547ecdf9 --count 1 --instance-type t2.micro --security-group-ids sg-01ce2b8e86bbaffcb --associate-public-ip-address --subnet-id subnet-03977621d0242cbc5 --tag-specifications 'ResourceType=instance,Tags=[{Key=Name,Value=scrappy-clone}]'


Prerequisite Information
------------------------


 OS Supported:
------------
*Microsoft Windows Server 2003 (Standard, Datacenter, Enterprise) with Service Pack 1 (SP1) or later (32- and 64-bit)*

*Microsoft Windows Server 2003 R2 (Standard, Datacenter, Enterprise) (32- and 64-bit)*

*Microsoft Windows Server 2008 (Standard, Datacenter, Enterprise) (32- and 64-bit)*

*Microsoft Windows Server 2008 R2 (Standard, Datacenter, Enterprise) (64-bit only)*

*Microsoft Windows Server 2012 (Standard, Datacenter) (64-bit only)*

*Microsoft Windows Server 2012 R2 (Standard, Datacenter) (64-bit only) (Nano Server installation not supported)*

*Microsoft Windows Server 2016 (Standard, Datacenter) (64-bit only)*

*Red Hat Enterprise Linux (RHEL) 5.1-5.11, 6.1-6.9, 7.0-7.3 (6.0 lacks required drivers)*

*SUSE Linux Enterprise Server 11 with Service Pack 1 and kernel 2.6.32.12-0.7*

*SUSE Linux Enterprise Server 11 with Service Pack 2 and kernel 3.0.13-0.27*

*SUSE Linux Enterprise Server 11 with Service Pack 3 and kernel 3.0.76-0.11, 3.0.101-0.8, or 3.0.101-0.15*

*SUSE Linux Enterprise Server 11 with Service Pack 4 and kernel 3.0.101-63*

Formats Supported:
-----------------
- OVA *(Open Virtual Appliance)*
- VMDK *(Virtual Machine Disk)*
- VHD/VHDX *(Fixed and Dynamic Virtual Hard Disk)*


Supported Instance Types:
-------------------------
Linux Supported:

General purpose: t2.micro | t2.small | t2.medium | m3.medium | m3.large | m3.xlarge | m3.2xlarge

Compute optimized: c3.large | c3.xlarge | c3.2xlarge | c3.4xlarge | c3.8xlarge | cc1.4xlarge | cc2.8xlarge
Memory optimized: r3.large | r3.xlarge | r3.2xlarge | r3.4xlarge | r3.8xlarge | cr1.8xlarge

Storage optimized: i2.xlarge | i2.2xlarge | i2.4xlarge | i2.8xlarge | hi1.4xlarge | hi1.8xlarge

Accelerated computing: cg1.4xlarge

Windows Supported:
Mostly ALL



Originating OS File-systems supported:
------------------------------------
Windows: (32 and 64bit)
MBR-partitioned volumes and GUID Partition Table (GPT) partitioned volumes that are formatted using the NTFS file system.
For GPT-partitioned volumes, only VHDX is supported as an image format.

Linux:
MBR-partitioned volumes that are formatted using the ext2, ext3, ext4, Btrfs, JFS, or XFS file system.
GUID Partition Table (GPT) partitioned volumes are not supported




Licensing:
---------

Auto (default) Detects the source-system operating system and applies the appropriate license to the migrated virtual machine 

- AWS -  Replaces the source-system license with an AWS license, if appropriate, on the migrated VM.
- BYOL - Retains the source-system license, if appropriate, on the migrated VM.

**Note: Linux operating systems support only BYOL licenses. Choosing Auto means that a BYOL license is used.**

- Migrated Red Hat Enterprise Linux (RHEL) VMs must use Cloud Access (BYOL) licenses. For more information, see Red Hat Cloud Access on the Red Hat website.

- Migrated SUSE Linux Enterprise Server VMs must use SUSE Public Cloud Program (BYOS) licenses. For more information, see SUSE Public Cloud Program--Bring Your Own Subscription.

**Note: Windows server operating systems support either BYOL or AWS licenses.**

- If you choose Auto (the default), the AWS license will be used if the VM has a server OS. Otherwise, the BYOL license is used.
