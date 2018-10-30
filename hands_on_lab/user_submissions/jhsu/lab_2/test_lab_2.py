import json
import yaml
import boto3

from moto import mock_iam

import lab_2_def as iam

NewUser = 'jhsu-lab-2-boto3-user2'

@mock_iam
def test_mock_create_use():
   iam_client   = boto3.client('iam')
   iam_create_user_response = iam.iam_create_user(iam_client, NewUser)
   print(iam_create_user_response)
   assert NewUser == iam_create_user_response['User']['UserName']
#  assert False


@mock_iam
def test_mock_delete_use():
   iam_client   = boto3.client('iam')
   UserName = iam.iam_create_user(iam_client, NewUser)
   iam_delete_user_response = iam.iam_delete_user(iam_client, NewUser)
   assert iam_delete_user_response is None




