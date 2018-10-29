import json
import yaml
import boto3

from moto import mock_s3

import lab_1_s3_def as s3

test_bucket= 'jhsu-s3-boto3-bucket1'

@mock_s3
def test_mock_create_bucket():
   s3_client = boto3.client('s3')
   s3_bucket_url = s3.s3_create_bucket(s3_client, test_bucket)
   print(s3_bucket_url)
   assert s3_bucket_url.find('https://')
#  assert False

@mock_s3
def test_mock_delete_bucket():
   s3_client = boto3.client('s3')
   s3_bucket_url = s3.s3_create_bucket(s3_client, test_bucket)
   s3_pass_pattern = 's3_delete_bucket_passed'
   s3_bucket_url = s3.s3_create_bucket(s3_client, test_bucket)
   s3_delete_bucket_response = s3.s3_delete_bucket(s3_client, test_bucket)
   print()
   print(s3_delete_bucket_response)
   final_s3_pass_pattern = s3_pass_pattern + '_' + str(s3_delete_bucket_response)
   print()
   print(final_s3_pass_pattern)
   assert final_s3_pass_pattern == s3_pass_pattern +'_None'
#  assert False


