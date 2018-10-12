#!/home/drivera/python/python36/bin/python3

import boto3

client = boto3.client('iam')



def createuser():
    userexist = client.get_user['UserName']
    for user in userexist:
        if userexist == userexist:
              
              print('User Exist')
        else:
          response = client.create_user(
          Path='/',
        UserName='iam-david-user-py'
)
        user_response = client.list_users(
	PathPrefix='/'
)
        #        print('Creating IAM User')
         #   print('-----------------------')
          #  print(response)
createuser()


print('')
print('')
def creategroup():
    usergroup = client.create_group(
        Path='/',
        GroupName='iam-david-group-py'
)
    print('Creating IAM Group')
    print('---------------------------')
    print(usergroup)
creategroup()


def usertogroup():
    groupadd = client.add_user_to_group(
    GroupName='iam-david-group-py',
    UserName='iam-david-user-py'
)
    print('')
    print('Add IAM user to Group')
    print('--------------------------')
    print(groupadd)
usertogroup()


def remfromgroup():
    groupdel = client.remove_user_from_group(
    GroupName='iam-david-group-py',
    UserName='iam-david-user-py'
)
    print('')
    print('Delete IAM user from Group')
    print('--------------------------')
    print(groupdel)
remfromgroup()


def deleteuser():
    response = client.delete_user(
    UserName='iam-david-user-py'
)
    #print(response)
deleteuser()


def delgroup():
    group = client.delete_group(
    GroupName='iam-david-group-py'
)
    print('')
    print('Delete IAM Group')
    print('---------------------')
    print(group)
delgroup()

