AWS boto3 Python SDK
====================

Goals

- Access AWS service through boto3 Python SDK
- Access S3 bucket creation/deletion service

Prerequisites

- Python3 installation (virtual environment)
- ait-training account access with MFA authentication
- aws-shelltools package installed

Reference
- boto3 documentation https://boto3.amazonaws.com/v1/documentation/api/latest/index.html


Assume role into ait-training account
---------------------------------------------

From Python virtual enviroment, Assume role in ait-training account::

  # Enter Python virtual environment
  $ cd
  $ alias py3
  $ alias py3='source ~/python/py3/bin/activate'
  $ py3
  (py3) $ python -V

  # Check current aws iam user status
  (py3) $ aws-refresh
  (py3) $ aws-drop-assumed-role
  (py3) $ aws-whoami

  # Assume role into ait-traing account
  (py3) $ aws-list-rols
  (py3) $ aws-assume-role ait-training-xxxx
  (py3) $ aws-whoami

Access AWS/S3 service with boto3 SDK
------------------------------------

boto is the Amazon Web Services (AWS) SDK for Python, 
which allows Python developers to write software that makes use of 
Amazon services like S3 and EC2. Boto provides an easy to use, 
object-oriented API as well as low-level direct service access.  ::

  # boto3 related packages should have been installed
  (py3) $ pip list | grep oto
  (py3) $ boto3                    1.9.28
  (py3) $ botocore                 1.12.28


Following boto3/s3 client object methods are defined in boto3 SDK::

 class S3.Client

    A low-level client representing Amazon Simple Storage Service (S3):

    import boto3

    client = boto3.client('s3')

    These are the available methods:

        abort_multipart_upload()
        can_paginate()
        complete_multipart_upload()
        copy()
        copy_object()
        create_bucket()
        create_multipart_upload()
        delete_bucket()
        delete_bucket_analytics_configuration()
        delete_bucket_cors()
        delete_bucket_encryption()
        delete_bucket_inventory_configuration()
        delete_bucket_lifecycle()
        delete_bucket_metrics_configuration()
        delete_bucket_policy()
        delete_bucket_replication()
        delete_bucket_tagging()
        delete_bucket_website()
        delete_object()
        delete_object_tagging()
        delete_objects()
        delete_public_access_block()
        download_file()
        download_fileobj()
        generate_presigned_post()
        generate_presigned_url()
        get_bucket_accelerate_configuration()
        get_bucket_acl()
        get_bucket_analytics_configuration()
        get_bucket_cors()
        get_bucket_encryption()
        get_bucket_inventory_configuration()
        get_bucket_lifecycle()
        get_bucket_lifecycle_configuration()
        get_bucket_location()
        get_bucket_logging()
        get_bucket_metrics_configuration()
        get_bucket_notification()
        get_bucket_notification_configuration()
        get_bucket_policy()
        get_bucket_policy_status()
        get_bucket_replication()
        get_bucket_request_payment()
        get_bucket_tagging()
        get_bucket_versioning()
        get_bucket_website()
        get_object()
        get_object_acl()
        get_object_legal_hold()
        get_object_lock_configuration()
        get_object_retention()
        get_object_tagging()
        get_object_torrent()
        get_paginator()
        get_public_access_block()
        get_waiter()
        head_bucket()
        head_object()
        list_bucket_analytics_configurations()
        list_bucket_inventory_configurations()
        list_bucket_metrics_configurations()
        list_buckets()
        list_multipart_uploads()
        list_object_versions()
        list_objects()
        list_objects_v2()
        list_parts()
        put_bucket_accelerate_configuration()
        put_bucket_acl()
        put_bucket_analytics_configuration()
        put_bucket_cors()
        put_bucket_encryption()
        put_bucket_inventory_configuration()
        put_bucket_lifecycle()
        put_bucket_lifecycle_configuration()
        put_bucket_logging()
        put_bucket_metrics_configuration()
        put_bucket_notification()
        put_bucket_notification_configuration()
        put_bucket_policy()
        put_bucket_replication()
        put_bucket_request_payment()
        put_bucket_tagging()
        put_bucket_versioning()
        put_bucket_website()
        put_object()
        put_object_acl()
        put_object_legal_hold()
        put_object_lock_configuration()
        put_object_retention()
        put_object_tagging()
        put_public_access_block()
        restore_object()
        select_object_content()
        upload_file()
        upload_fileobj()
        upload_part()
        upload_part_copy()


Python modules defined in this workshop session::

  # Mutiple python modules are defined in the working directory
  (py3) $ ls -l *py
  lab_1_s3_def.py
  lab_1_s3_main.py
  myutil.py
  (py3) $

  # lab_1_s3_def.py  : call out boto3 methods for s3 bucket listing/creation/deletion
  # lab_1_s3_main.py : executable python main module to exercise boto3 functions
  # myutil.py        : print function called out from main module


S3 bucket creation/deletion functions::

  (py3) $ cat lab_1_s3_def.py

  def s3_list_buckets(s3_client):
     s3_buckets = s3_client.list_buckets()
     bucket_list = []
     bucket_count = 0
     for bucket in s3_buckets['Buckets']:
        bucket_list.append(bucket['Name'])
     bucket_count = len(bucket_list)
     return (bucket_list, bucket_count)


  def s3_check_bucket_in_list(s3_client, test_bucket):
     s3_buckets = s3_client.list_buckets()
     bucket_list = []
     bucket_count = 0
     for bucket in s3_buckets['Buckets']:
        bucket_list.append(bucket['Name'])
     if test_bucket in bucket_list:
        return True
     else:
        return False


  def s3_create_bucket(s3_client,NewBucket):
     s3_create_bucket_response = s3_client.create_bucket(
     Bucket = NewBucket,
     CreateBucketConfiguration={'LocationConstraint':'us-west-2'})
     return s3_create_bucket_response


  def s3_delete_bucket(s3_client,OldBucket):
     s3_delete_bucket_response = s3_client.delete_bucket(Bucket = OldBucket)
     return s3_delete_bucket_response['ResponseMetadata']


main function to call out above functions::

  (py3) $ cat lab_1_s3_main.py

  #! /usr/bin/env python

  import time
  import boto3
  import json
  import yaml

  import myutil as util
  import lab_1_s3_def as s3

  if __name__ == "__main__":

     s3_resource = boto3.resource('s3')
     s3_client   = boto3.client('s3')

     test_bucket= 'jhsu-s3-boto3-bucket1'
     test_file  = 'jhsu-s3-boto3-file1'
     print()

     print("--- S3 bucket list ---")
     (s3_bucket_list, s3_bucket_cnt) = s3.s3_list_buckets(s3_client)
     util.s3_print_bucket_list(s3_bucket_list)

     print("--- S3 create bucket ---")
     s3_create_bucket_response = s3.s3_create_bucket(s3_client, test_bucket)

     print("--- Validate bucket creation ---")
     if s3.s3_check_bucket_in_list(s3_client, test_bucket):
        print(" Bucket creation passed! ")
     else:
        print(" Bucket creation failed! ")

     print("--- S3 bucket list ---")
     (s3_bucket_list, s3_bucket_cnt) = s3.s3_list_buckets(s3_client)
     util.s3_print_bucket_list(s3_bucket_list)

     print("--- S3 delete bucket ---")
     s3_delete_bucket_response = s3.s3_delete_bucket(s3_client, test_bucket)

     print("--- Validate bucket deletion ---")
     if s3.s3_check_bucket_in_list(s3_client, test_bucket):
        print(" Bucket deletion failed! ")
     else:
        print(" Bucket deletion passed! ")

     print("--- S3 bucket list ---")
     (s3_bucket_list, s3_bucket_cnt) = s3.s3_list_buckets(s3_client)
     util.s3_print_bucket_list(s3_bucket_list)


Test AWS S3 service
---------------------------------------------

Run python main() executable to create/delete AWS S3 bucket::

  # In the working directory
  (py3) $ chmod u+x ./lab_1_s3_main.py
  (py3) $ ./lab_1_s3_main.py


   --- S3 bucket list ---

   S3 bucket cnt is 1
         stackset-91744a37-5269-432e-b4d0-40f-configbucket-cq1rauyo7t73

   --- S3 create bucket ---
   --- Validate bucket creation ---
    Bucket creation passed!
   --- S3 bucket list ---

   S3 bucket cnt is 2
         jhsu-s3-boto3-bucket1
         stackset-91744a37-5269-432e-b4d0-40f-configbucket-cq1rauyo7t73

   --- S3 delete bucket ---
   --- Validate bucket deletion ---
    Bucket deletion passed!
   --- S3 bucket list ---

   S3 bucket cnt is 1
         stackset-91744a37-5269-432e-b4d0-40f-configbucket-cq1rauyo7t73

  (py3)



