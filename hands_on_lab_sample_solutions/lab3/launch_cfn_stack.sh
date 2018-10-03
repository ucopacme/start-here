#! /bin/bash

# Create or update CloudFormation stack "ashtest-ec2"
# Usage:
#   ./launch_cfn_stack.sh
#   ./launch_cfn_stack.sh update

ACTION=$1
if [ $# != 1 ]; then
  ACTION=create
fi
if [ $ACTION != 'create' -a $ACTION != 'update' ]; then
  echo "action must be 'create' or 'update'"  
  exit 0
fi

SSHKEY=ashley@isis
SECURITY_GROUP=sg-0e19a5c91255a49ba

aws cloudformation ${ACTION}-stack \
  --stack-name ashtest-ec2 \
  --template-body file://./cfn-launch_ec2_instance.yaml \
  --parameters ParameterKey=KeyName,ParameterValue=$SSHKEY ParameterKey=SecurityGroupIds,ParameterValue=$SECURITY_GROUP \
  --tags Key=Name,Value=ashtest


exit


# Notes:
# 
# # to validate template syntax:
# aws cloudformation validate-template --template-body file://./cfn-launch_ec2_instance.yaml
#
# # to delete my stack run:
# aws cloudformation delete-stack --stack-name ashtest-ec2
