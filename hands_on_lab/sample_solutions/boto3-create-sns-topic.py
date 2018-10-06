#!/bin/env python 
import sys
import boto3 
import yaml


#TOPIC_NAME=ashtest-01


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
    topic_arn = [arn['TopicArn'] for arn in response['Topics'] if arn['TopicArn'].split(':')[-1] == topic_name][0]
    return topic_arn

                
if __name__ == '__main__':

    if len(sys.argv) > 2:
        action = sys.argv[1]
        topic_name = sys.argv[2]
    else:
        sys.exit(usage())

    if action == 'create':
        print(yamlfmt(create_sns_topic(topic_name)))

    elif action == 'report':
        topic_arn = get_topic_arn(topic_name)
        print(topic_arn)

    elif action == 'delete':
        print(action)

    else:
        sys.exit(usage())
