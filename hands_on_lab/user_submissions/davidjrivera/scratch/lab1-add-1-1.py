#!/bin/env python

import boto3


def createuser():
    client = boto3.client('iam')
    response = client.create_user(Path='/', UserName='iam-david-user-py')
    #response = client.create_user(UserName='iam-david-group-py')
    user_response = client.list_users(PathPrefix='/')
    return response 

def creategroup():
    client = boto3.client('iam')
    usergroup = client.create_group(Path='/', GroupName='iam-david-group-py')
    return usergroup

def usertogroup():
    client = boto3.client('iam')
    groupadd = client.add_user_to_group(GroupName='iam-david-group-py',UserName='iam-david-user-py')
    return groupadd

def main():
    result = createuser()
    print('Creating IAM User')
    print('-----------------------')
    print (result)

    groupresult = creategroup()
    print('Creating IAM Group')
    print('---------------------------')
    print (groupresult)

    result = usertogroup()
    print('Add IAM user to Group')
    print('--------------------------')
    print(result)

if __name__ == "__main__":
    main()
