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


@mock_iam
def test_mock_list_use():
   iam_client   = boto3.client('iam')
   iam_create_user_response = iam.iam_create_user(iam_client, NewUser)
   (user_list, user_count) = iam.iam_list_users(iam_client)
   assert iam.iam_check_user_in_list(iam_client, NewUser) and \
          not iam.iam_check_user_in_list(iam_client, 'non_user')




