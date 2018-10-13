import json
import yaml
import boto3

from moto import mock_iam

import lab_2_def as iam

NewUser = 'jhsu-lab-1-boto3-user1'

iam_client   = boto3.client('iam')

@mock_iam
def test_mock_create_use():
   UserName = iam.iam_create_user(iam_client, NewUser)
   print(UserName)
   assert NewUser == UserName
#  assert False

@mock_iam
def test_mock_delete_use():
   iam_delete_user_response = iam.iam_delete_user(iam_client, NewUser)
   print(iam_delete_user_response)
   assert iam_delete_user_response['ResponseMetadata']['HTTPStatusCode'] == 200
#  assert False



