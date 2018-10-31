import boto3

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


