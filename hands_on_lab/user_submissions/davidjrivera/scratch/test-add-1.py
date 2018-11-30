#!/home/drivera/python/python36/bin/python3
import boto3
client = boto3.client('iam')

def createuser():
    response = client.create_user(
       Path='/',
       UserName='iam-david-user-py'
)
    user_response = client.list_users(
        PathPrefix='/'
)
    print('Creating IAM User')
    print('-----------------------')
    print(response)
createuser()

def test_createuser():
    assert createuser() == 'iam-david-user-py'

def func():
    return(5)
 
def test_func():
    assert func() == 4
