import boto3
import json
import yaml

from moto import mock_s3

import lab_1_s3_def as s3

test_bucket= 'jhsu-s3-boto3-bucket1'

@mock_s3
def test_mock_create_bucket():
   s3_client = boto3.client('s3')
   s3_create_bucket_response = s3.s3_create_bucket(s3_client, test_bucket)
   print(s3_create_bucket_response)
   assert s3_create_bucket_response['ResponseMetadata']['HTTPStatusCode'] == 200


@mock_s3
def test_mock_delete_bucket():
   s3_client = boto3.client('s3')
   s3_create_bucket_response = s3.s3_create_bucket(s3_client, test_bucket)
   s3_delete_bucket_response = s3.s3_delete_bucket(s3_client, test_bucket)
   print(s3_delete_bucket_response)
   assert s3_delete_bucket_response['HTTPStatusCode'] == 204


@mock_s3
def test_mock_list_bucket():
   s3_client = boto3.client('s3')
   s3_create_bucket_response = s3.s3_create_bucket(s3_client, test_bucket)
   (bucket_list, bucket_count) = s3.s3_list_buckets(s3_client)
   assert s3.s3_check_bucket_in_list(s3_client, test_bucket) and \
	  not s3.s3_check_bucket_in_list(s3_client, 'non_bucket')


