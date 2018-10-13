
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

def iam_list_groups(iam_client):
   iam_groups = iam_client.list_groups()
   group_list = []
   group_count = 0
   for group in iam_groups['Groups']:
      group_list.append(group['GroupName'])
   group_count = len(group_list)
   return (group_list, group_count)


def iam_list_users(iam_client):
   print()
   print("--- IAM users ---")
   iam_users = iam_client.list_users()
#  print('iam list_users() response:')
#  for item in list(iam_users.items()):
#     (key, value) = item
#     print("-- ", key, ":", value)
#  print()
   print('iam user list:')
   user_list = []
   user_count = 0
   for user in iam_users['Users']:
      print('\t',user)
   print()
   print('iam user name:')
   for user in iam_users['Users']:
      print('\t', user ['UserName'])
      user_list.append(user['UserName'])
   user_count = len(user_list)
   return (user_list, user_count)

def iam_create_user(iam_client,NewUser):
   print()
   print("--- IAM create user:", NewUser, "---")
   iam_create_user = iam_client.create_user(UserName = NewUser)
   print()
   print('iam create_user() response:')
   for item in list(iam_create_user.items()):
      (key, value) = item
      print('\t', key, ":", value)
   print()
   return iam_create_user['User']['UserName']

def iam_delete_user(iam_client,OldUser):
#  OldUser = 'jhsu-iam-boto3-user1'
   print()
   print("--- IAM deleter user:", OldUser, "---")
   iam_delete_user = iam_client.delete_user(UserName = OldUser)
   print()
   print('iam_delete_user() response:')
   for item in list(iam_delete_user.items()):
      (key, value) = item
      print('\t', key, ":", value)
   return iam_delete_user 

def iam_create_group(iam_client, Group):
   print()
   print("--- IAM creat group", Group, "---")
   iam_create_group = iam_client.create_group(GroupName = Group)
   print()
   print('iam_create_group() response:')
   for item in list(iam_create_group.items()):
      (key, value) = item
      print('\t', key, ":", value)
   print()
   return

def iam_delete_group(iam_client,OldGroup):
#  OldUser = 'jhsu-iam-boto3-user1'
   print()
   print("--- IAM deleter group:", OldGroup, "---")
   iam_delete_group = iam_client.delete_group(GroupName = OldGroup)
   print()
   print('iam_delete_group() response:')
   for item in list(iam_delete_group.items()):
      (key, value) = item
      print('\t', key, ":", value)
   return

def iam_add_user_to_group(iam_client, Group, User):
   print()
   print("--- IAM add user", User, "to group", Group, "---")
   iam_add_user_to_group =  iam_client.add_user_to_group(GroupName = Group, UserName = User)
   print()
   print('iam add_user_to_group() response:')
   for item in list(iam_add_user_to_group.items()):
      (key, value) = item
      print('\t', key, ":", value)
   print()
   return

def iam_remove_user_from_group(iam_client, Group, User):
   print()
   print("--- IAM remove user ", User, "remove group", Group, "---")
   iam_remove_user_from_group =  iam_client.remove_user_from_group(GroupName = Group, UserName = User)
   print()
   print('iam_remove_user_from_group() response:')
   for item in list(iam_remove_user_from_group.items()):
      (key, value) = item
      print('\t', key, ":", value)
   print()
   return

