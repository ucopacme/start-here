#!/bin/env python

#
# Usage: ./lab1-add-01.py
#

import boto3
import yaml


from moto import mock_s3

from lab1_add import creates3
from lab1_add import dels3


def yamlfmt(obj):
    if isinstance(obj, str):
        return obj
    return yaml.dump(obj, default_flow_style=False)

@mock_s3
def test_creates3():
     s3 = boto3.client('s3')
     new_bucket = 'lab1davidpythons3'
     response =  s3.create_bucket( Bucket=new_bucket,  CreateBucketConfiguration={'LocationConstraint': 'us-west-2'})
     assert response['ResponseMetadata']['HTTPStatusCode'] == 200
 
@mock_s3
def test_dels3():
      s3 = boto3.client('s3')
      new_bucket = 'lab1davidpythons3'
      response =  s3.create_bucket( Bucket=new_bucket,  CreateBucketConfiguration={'LocationConstraint': 'us-west-2'})
      delbuck = s3.delete_bucket(Bucket='lab1davidpythons3')
      assert delbuck['ResponseMetadata']['HTTPStatusCode'] == 204
