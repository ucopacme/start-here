#!/bin/env python

#
# Usage: ./lab2-add-01.py
#

import boto3
import yaml


def yamlfmt(obj):
    if isinstance(obj, str):
        return obj
    return yaml.dump(obj, default_flow_style=False)

def createuser(iam_user):
    client = boto3.client('iam')
    response = client.create_user(Path='/', UserName=iam_user)
    return response 

def deleteuser(iam_user):
    client = boto3.client('iam')
    deluser = client.delete_user(UserName=iam_user)
    print(deluser)
    return deluser


def main():
    user = 'iam-david-user-py'
    result = createuser(user)
    print('Creating IAM User')
    print('-----------------------')
    print(yamlfmt(result['User']))

    
    user = 'iam-david-user-py'
    result = deleteuser(user)

if __name__ == "__main__":
    main()
