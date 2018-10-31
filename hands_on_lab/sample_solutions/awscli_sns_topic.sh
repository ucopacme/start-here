#!/bin/bash
#set -x

# create, validate and delete AWS SNS topic with awscli

TOPIC_NAME=ashtest-01

echo
echo "create SNS topic"
topic_arn=$(aws sns create-topic --name $TOPIC_NAME | grep TopicArn| awk '{print $2}' | tr -d '"')
echo $topic_arn

echo
echo "validate SNS topic"
aws sns get-topic-attributes --topic-arn $topic_arn

echo
echo "delete SNS topic"
aws sns delete-topic --topic-arn $topic_arn
