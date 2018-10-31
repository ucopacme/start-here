#!/bin/bash
#

aws cloudformation validate-template --template-body file://./cfn_sns_topic.yaml
echo "creating stack"
aws cloudformation create-stack --stack-name sns-topic-ashtest-01 --template-body file://./cfn_sns_topic.yaml
aws cloudformation describe-stacks --stack-name sns-topic-ashtest-01

sleep 20
aws cloudformation describe-stacks --stack-name sns-topic-ashtest-01

echo;echo
echo "deleting stack"
aws cloudformation delete-stack --stack-name sns-topic-ashtest-01
aws cloudformation describe-stacks --stack-name sns-topic-ashtest-01

sleep 10
aws cloudformation describe-stacks --stack-name sns-topic-ashtest-01





