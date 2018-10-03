#!/bin/bash

# Launch EC2 instance using AWS CLI into the default VPC/Subnet


# Set params based on your specific account and vpc
AMI=ami-6cd6f714
REGION=us-west-2
SECURITY_GROUP=sg-0e19a5c91255a49ba
SSHKEY=ashley@isis


aws ec2 run-instances \
	--image-id $AMI \
	--count 1 \
	--instance-type t2.micro \
	--key-name $SSHKEY \
	--security-group-ids $SECURITY_GROUP

exit

Notes:

hands_on_lab/lab3> aws ec2 describe-instances --instance-ids i-09233569929a572a7 | grep PublicIp
                    "PublicIpAddress": "18.236.174.51",


agould@horus:~ > ssh ec2-user@18.236.174.51
Warning: Permanently added '18.236.174.51' (ECDSA) to the list of known hosts.
Enter passphrase for key '/home/agould/.ssh/id_rsa':

       __|  __|_  )
       _|  (     /   Amazon Linux 2 AMI
      ___|\___|___|

https://aws.amazon.com/amazon-linux-2/
5 package(s) needed for security, out of 338 available
Run "sudo yum update" to apply all updates.
[ec2-user@ip-172-31-27-156 ~]$


hands_on_lab/lab3> aws ec2 terminate-instances --instance-ids i-09233569929a572a7
{
    "TerminatingInstances": [
        {
            "CurrentState": {
                "Code": 32,
                "Name": "shutting-down"
            },
            "InstanceId": "i-09233569929a572a7",
            "PreviousState": {
                "Code": 16,
                "Name": "running"
            }
        }
    ]
}

