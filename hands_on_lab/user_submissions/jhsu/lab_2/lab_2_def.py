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


if __name__ == "__main__":
    iam_client   = boto3.client('iam')
    NewUser = 'ashleytestingjhsu'
    UserName = iam_create_user(iam_client, NewUser)
    iam_delete_user(iam_client, UserName)
