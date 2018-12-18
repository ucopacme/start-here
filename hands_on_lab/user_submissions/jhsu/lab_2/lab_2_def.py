
def iam_list_users(iam_client):
   iam_list_users_response = iam_client.list_users()
   user_list = []
   for User in iam_list_users_response['Users']:
      user_list.append(User['UserName'])
   list_count = len(user_list)
   return (user_list, list_count)


def iam_create_user(iam_client,NewUser):
   iam_create_user_response = iam_client.create_user(UserName = NewUser)
   return iam_create_user_response


def iam_check_user_in_list(iam_client, test_user):
   iam_list_users_response = iam_client.list_users()
   user_list = []
   for User in iam_list_users_response['Users']:
      user_list.append(User['UserName'])
   list_count = len(user_list)
   if test_user in user_list:
      return True
   else:
      return False


def iam_delete_user(iam_client,OldUser):
   iam_delete_user = iam_client.delete_user(UserName = OldUser)
   return 


