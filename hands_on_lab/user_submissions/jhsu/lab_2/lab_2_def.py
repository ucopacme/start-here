import boto3
'''
def jsonfmt(obj, default=to_serializable):
    if isinstance(obj, str):
        return obj
    return json.dumps(
        obj,
        indent=4,
        separators=(',', ': '),
        default=default,
)
'''

#def jsonfmt(obj, default=to_serializable):
def jsonfmt(obj):
    if isinstance(obj, str):
        return obj
    return json.dumps(
        obj,
        indent=4,
        separators=(',', ': ')
#       default=default 
    )

def yamlfmt(obj):
    if isinstance(obj, str):
        return obj
    return yaml.dump(obj, default_flow_style=False)


def iam_list_users(iam_client):
   iam_list_users_response = iam_client.list_users()
   user_list = []
   for User in iam_list_users_response['Users']:
      user_list.append(User['UserName'])
   print(user_list)
   print()
   return


def iam_create_user(iam_client,NewUser):
   iam_create_user_response = iam_client.create_user(UserName = NewUser)
   return iam_create_user_response


def iam_check_user_in_list(iam_response, test_user):
   iam_user_list = iam_response['User']
   print('iam user:  ' + iam_user_list)
   return


def iam_delete_user(iam_client,OldUser):
   iam_delete_user = iam_client.delete_user(UserName = OldUser)
   return 

'''
if __name__ == "__main__":

    iam_client   = boto3.client('iam')

    User1 = 'John'
    User2 = 'Michael'

    print("--- IAM list users: ---")
    iam_list_users_response = iam_list_users(iam_client)
 
    print("--- IAM create user:", User1, "---")
    iam_create_user_response  = iam_create_user(iam_client, User1)

    print("--- IAM list users: ---")
    iam_list_users_response = iam_list_users(iam_client)
 
    print("--- IAM create user:", User2, "---")
    iam_create_user_response  = iam_create_user(iam_client, User2)

    print("--- IAM list users: ---")
    iam_list_users_response = iam_list_users(iam_client)
 
    print("--- IAM delete user: ---")
    iam_delete_user(iam_client, User1)
    print("--- IAM delete user: ---")
    iam_delete_user(iam_client, User2)

    print("--- IAM list users: ---")
    iam_list_users_response = iam_list_users(iam_client)
''' 

