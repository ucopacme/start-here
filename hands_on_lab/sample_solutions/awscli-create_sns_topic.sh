#!/bin/bash
set -x

# create, validate and delete AWS SNS topic with awscli

TOPIC_NAME=ashtest-01
topic_arn=$(aws sns create-topic --name $TOPIC_NAME | grep TopicArn| awk '{print $2}' | tr -d '"')
echo $topic_arn
aws sns get-topic-attributes --topic-arn $topic_arn
aws sns delete-topic --topic-arn $topic_arn
aws sns list-topics
