#! /home/jhsu/python/py3/bin/python3

import time
import boto3
import json
import yaml

import lab_1_s3_def as s3


if __name__ == "__main__":

   s3_resource = boto3.resource('s3')
   s3_client   = boto3.client('s3')

   test_bucket= 'jhsu-s3-boto3-bucket1'
   test_file  = 'jhsu-s3-boto3-file1'
   print()
  
   print("--- original S3 bucket list ---")
   (s3_bucket_list, s3_bucket_cnt) = s3.s3_list_buckets(s3_client)
   s3.s3_print_bucket_list(s3_bucket_list)

   print("--- S3 create bucket ---")
   s3_create_bucket_response = s3.s3_create_bucket(s3_client, test_bucket)

   print("--- Validate bucket creation ---")
   s3.s3_check_bucket_in_list(s3_create_bucket_response, test_bucket)
   (s3_bucket_list, s3_bucket_cnt) = s3.s3_list_buckets(s3_client)
   s3.s3_print_bucket_list(s3_bucket_list)

   print("--- S3 delete bucket ---")
   s3_delete_bucket_response = s3.s3_delete_bucket(s3_client, test_bucket)

   print("--- Validate bucket deletion ---")
   s3.s3_check_bucket_deleteion(s3_delete_bucket_response)
   (s3_bucket_list, s3_bucket_cnt) = s3.s3_list_buckets(s3_client)
   s3.s3_print_bucket_list(s3_bucket_list)
   
