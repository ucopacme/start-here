Lab 4B - CloudFormation Lab using AWS CLI
=========================================

**Context:**
In this Lab you will be utilizing the AWS CLI commands developed by AWS. 

**Goals:**
- We will be creating an AWS EC2 web server that is serving a web page.
- You will also be able to log into the EC2 instance and play around.

**Lay Out of Lab**
This Lab will have you fill in information into the **base** CloudFomration Template.  
**NOTE** In this Lab we will be using the YAML format. It must be said that the indentation is EXTREMELY particular. If something is not working, it probably is the issue.


Prerequisites for this lab
-------------------------
- Lab 1 - AWS Console Lab
- Lab 2 - Cloud9 and AWS CLI
- Lab 3 - Linux Workstation Setup
- Lab 4a - CloudFormation via the Console


Step 1) Downloading the CloudFormation Template
------------------------------------------------
Step 1) Download a copy of the CloudFormation template from the S3 Bucket
       ** Note: Due to GitHub being a public site, only examples of syntax are given. You will be given a sheet with pertenant info**

- The file you need to download is called: **cf-awscli-template.yml**

To download the file you will use the command: aws s3 sync s3://mys3bucket/ . --exclude "*" --include "cf-awscli-template.yml"

**NOTE:** It will download it to your CWD
::

 (python36) [user@aws examples]$ ls
 (python36) [user@aws examples]$ aws s3 sync s3://mys3bucket/ . --exclude "*" --include "cf-awscli-template.yml"
 download: s3://mys3bucket/cf-awscli-template.yml to ./cf-awscli-template.yml
 (python36) [user@aws examples]$ ls
 cf-awscli-template.yml


Step 2) Updating the CloudFormation Template
---------------------------------------------
The downloaded CloudFormation Template will be used to build a new CloudFormation Stack. However, we first need to make some updates to the template. In order to allow you to understand how this works, some pertenant information was left out that you must fill in based off information provided to you in a seperate handout.

The information you must fill into the template is:

- VPC Id
- SubNet Id
- SecurectyGroup Id
- your personal KeyName
- tag   Name  (Value)

** Notice in the snipit of the info you see (Insert * ID HERE) this is the information you must change.
::

 (python36) [user@aws examples]$ vi cf-awscli-template.yml

 Description: >
        AWS Scrum Team - One day Workshop on CloudFormation
 Parameters:
  ec2VPC:
    Description: VPC to be used - starting with existing VPC
    Type: String
    Default: (Insert VPC ID HERE)

  ec2Subnet:
    Description: Subnet to be used within the UcopVPC
    Type: String
    Default: (Insert SUBNET ID here)
  ec2key:



Step 3) Verify the Cloudformation template is valid and usable
-------------------------------------------------------------
Once you have made the changes to the template as needed, it is good practice to verify that the template is actually usable. To do this we run this awscli command: **aws cloudformation validate-template**

**Example:** aws cloudformation validate-template --template-body file://cf-awscli-template.yml 

**Note:** The location of the template is in the location I am running the command or I would have to qualify th path.
::

 (python36) [user@raws example]$ aws cloudformation validate-template --template-body file://cf-awscli-template.yml
 {
    "Parameters": [
        {
            "ParameterKey": "ec2VPC",
            "DefaultValue": "(Insert VPC ID HERE)",
            "NoEcho": false,
            "Description": "VPC to be used - starting with existing VPC"
        },
        {
            "ParameterKey": "ec2Subnet",
            "DefaultValue": "(Insert SUBNET ID here)",
            "NoEcho": false,
            "Description": "Subnet to be used within the UcopVPC"
        },
        {
            "ParameterKey": "ec2key",
            "DefaultValue": "(insert Key name here)",
            "NoEcho": false,
            "Description": "Key Pair Required to Log into Instance after creation"
        }
    ],
    "Description": "AWS Scrum Team - One day Workshop on CloudFormation\n"


Looks like we are good!!

**NOTE:** this verification will only do a simple check on YAML and JSON formats, and for dependencies. If you have a miss-spelled word, this will not be caught till you attempt to create the stack. At that point the stack creation will fail.




Step 4) Build a CloudFormation Stack based off your CloudFormation Template
---------------------------------------------------------------------------

Now that we have modified the CloudFormation Template to be specific to  you. Let's create our stack.

The command needed to create the CloudFormation stack is: **aws cloudformation create-stack**

- You must give the Stack a name: use this structure: **john-cf-workshop**

**Example:** aws cloudformation create-stack --stack-name john-cf-workshop --template-body file://cf-awscli-template.yml

Now let's kick it off
::
 
 (python36) [user@aws example]$ aws cloudformation create-stack --stack-name john-cf-workshop --template-body file://cf-awscli-template.yml
 {
    "StackId": "arn:aws:cloudformation:us-west-2:071826132890:stack/john-cf-workshop/54120d70-fa5a-11e8-8a6c-503ac93168c5"
 }


Was the build successful?

let's find out..


Step 5) Verify your CloudFormation stack was successfully built
---------------------------------------------------------------

To verify that the stack you intended on building actually completed to success, we use the **aws cloudformation describe-stack** command

**Example** aws cloudformation describe-stacks  --stack-name john-cf-workshop
::


 (python36) [user@aws documents]$ aws cloudformation describe-stacks  --stack-name john-cf-workshop
 {
    "Stacks": [
        {
            "StackId": "arn:aws:cloudformation:us-west-2:011026131110:stack/john-cf-workshop/54120d70-fa5a-11e8-8a6c-503ac93168c5",
            "StackName": "john-cf-workshop",
            "Description": "AWS Scrum Team - One day Workshop on CloudFormation\n",
            "Parameters": [
                {
                    "ParameterKey": "ec2VPC",
                    "ParameterValue": "vpc-0e29e4573834rc65f75555c"
                },
                {
                    "ParameterKey": "ec2Subnet",
                    "ParameterValue": "subnet-04b5f4c5555b55070"
                },
                {
                    "ParameterKey": "ec2key",
                    "ParameterValue": "john-kp"
                }
            ],
            "CreationTime": "2018-12-07T19:57:29.937Z",
            "RollbackConfiguration": {},
            "StackStatus": "CREATE_COMPLETE",
            "DisableRollback": false,
            "NotificationARNs": [],
            "Tags": [],
            "EnableTerminationProtection": false
        }
    ]
}



** YUP IT LOOKS LIKE IT CREATED SUCCESSFULLY!!

I wonder if we can log into it using our key?


Step 6) Find out what your Public IP Address is
------------------------------------------------
Now that you have sucessfully built a CloudFormation Template and it is up and running, we have to query to find your Public IP Address:

- to find it, we use this command: **aws ec2 describe-instances** 

**Example:** aws ec2 describe-instances --filters "Name=tag:Name,Values=john-cf-ec2" 

**NOTE:** The one value you have to modify in the above command is: "Name=tag:Name,Values=(value-to-modify)" 

Search for your Public IP Address in the results of the command.
::

 (python36) [user@aws test]$ aws ec2 describe-instances --filters "Name=tag:Name,Values=john-cf-ec2"
 {
    "Reservations": [
        {
            "Groups": [],
            "Instances": [
                {
                    "AmiLaunchIndex": 0,
                    "ImageId": "ami-0d1000aff9a9bad89",
                    "InstanceId": "i-04a4999999995fefb",
                    "InstanceType": "t2.micro",
                    "KeyName": "john-kp",
                    "LaunchTime": "2018-12-07T22:36:58.000Z",
                    "Monitoring": {
                        "State": "disabled"
                    },
                    "Placement": {
                        "AvailabilityZone": "us-west-2a",
                        "GroupName": "",
                        "Tenancy": "default"
                    },
                    "PrivateDnsName": "ip-10-0-0-219.us-west-2.compute.internal",
                    "PrivateIpAddress": "10.0.0.219",
                    "ProductCodes": [],
                    "PublicDnsName": "ec2-64-62-76-25.us-west-2.compute.amazonaws.com",
                    "PublicIpAddress": "64.62.76.25",
                    "State": {
                    ....
                    ....
                    ....


We can see that our Public IP Address is: 64.62.76.25 **(yes this is a ficticious IP)**

Now that we know our IP, we can move onto logging into the EC2 instance...



Step 7) Logging into your EC2 instance using your keypair
---------------------------------------------------------

To log into the EC2 instance, we will have to use putty.

- you will have to use the key that is saved on your desktop from the previous labs. 
- open putty, use the public IP address, make sure your key is attached. To attach key, you go to SSH, than Auth under putty.
- Finally the user to log into the EC2 instance is username: **ec2-user**


Step 8) Verifying that the Web server is actaully serving data as you expected it to
------------------------------------------------------------------------------------
Go to a browser and see:
In a browser type: http://64.62.76.25



Step 9) Shutting down your EC2 instance
----------------------------------------
As a way to ensure we save money, the final step is to shutdown the EC2 instance.
To shutdown the EC2 instance we will use this command: aws ec2 stop-instances

**NOTE:** You can get the instance ID needed from the command previously used to find the IP Address.

To get instnance ID: aws ec2 describe-instances --filters "Name=tag:Name,Values=john-cf-ec2"
::

 (python36) [user@aws example]$ aws ec2 stop-instances --instance-ids i-04a49c6770305fefb
 {
    "StoppingInstances": [
        {
            "CurrentState": {
                "Code": 64,
                "Name": "stopping"
            },
            "InstanceId": "i-04a49c6770305fefb",
            "PreviousState": {
                "Code": 16,
                "Name": "running"
            }
        }
    ]
 } 


                           YOU ARE DONE WITH THIS LAB!!!


