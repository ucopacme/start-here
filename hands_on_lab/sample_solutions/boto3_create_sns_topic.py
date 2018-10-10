#!/bin/env python 
"""
Create or delete a named SNS topic.

Usage: ./boto3-create-sns-topic.py <action> <topic_name>
  where "action" is one of "create", "report" or "delete"

Examples:
  ./boto3-create-sns-topic.py create ashtest-01
  ./boto3-create-sns-topic.py report ashtest-01
  ./boto3-create-sns-topic.py delete ashtest-01

"""


import sys
import boto3 
import yaml


def usage():
    print('Usage: {} <action> <topic_name>\nwhere "action" is one of "create", "report" or "delete"'.format(sys.argv[0]))


def yamlfmt(obj):
    if isinstance(obj, str):
        return obj
    return yaml.dump(obj, default_flow_style=False)


def create_sns_topic(topic_name):
    sns_client = boto3.client('sns')
    response = sns_client.create_topic(Name=topic_name)
    return response['TopicArn']


def get_topic_arn(topic_name):
    sns_client = boto3.client('sns')
    response = sns_client.list_topics()
    topic_arn = (
        arn['TopicArn'] for arn in response['Topics'] 
        if arn['TopicArn'].split(':')[-1] == topic_name
    )
    return next(topic_arn, None)


def delete_sns_topic(topic_name):
    sns_client = boto3.client('sns')
    topic_arn = get_topic_arn(topic_name)
    if topic_arn is not None:
        print('deleting {}'.format(topic_arn))
        sns_client.delete_topic(TopicArn=topic_arn)

                
def main():
    if len(sys.argv) > 2:
        action = sys.argv[1]
        topic_name = sys.argv[2]
    else:
        sys.exit(usage())

    if action == 'create':
        print(yamlfmt(create_sns_topic(topic_name)))

    elif action == 'report':
        print(get_topic_arn(topic_name))

    elif action == 'delete':
        delete_sns_topic(topic_name)

    else:
        sys.exit(usage())


if __name__ == '__main__':
    main()
