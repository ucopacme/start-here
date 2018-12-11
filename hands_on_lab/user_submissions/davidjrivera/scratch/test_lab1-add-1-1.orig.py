#!/bin/env python

import boto3
import yaml

from moto import mock_iam

#client = boto3.client('iam')

#def yamlfmt(obj):
#    if isinstance(obj, str):
#        return obj
#    return yaml.dump(obj, default_flow_style=False)

@mock_iam
def createuser(iam_user):
    client = boto3.client('iam')
    response = client.create_user(Path='/', UserName=iam_user)
    return response
    assert 

#def creategroup():
#    client = boto3.client('iam')
#    usergroup = client.create_group(Path='/', GroupName='iam-david-group-py')
#    return usergroup

#def usertogroup(iam_grp , iam_user):
#    client = boto3.client('iam')
#    groupadd = client.add_user_to_group(GroupName=iam_grp, UserName=iam_user)
#    print(groupadd)
#    return groupadd

@mock_iam
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

    result = creategroup()
    print('Creating IAM Group')
    print('---------------------------')
    print (result)

#    user = 'iam-david-user-py'
#    group = 'iam-david-group-py'
#    result = usertogroup(group, user)

#    print('Add IAM user to Group')
#    print('--------------------------')
#    print(result)

    user = 'iam-david-user-py'
    result = deleteuser(user)

if __name__ == "__main__":
    main()

