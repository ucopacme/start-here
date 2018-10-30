
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


def s3_list_buckets(s3_client):
   s3_buckets = s3_client.list_buckets()
   bucket_list = []
   bucket_count = 0
   for bucket in s3_buckets['Buckets']:
      bucket_list.append(bucket['Name'])
   bucket_count = len(bucket_list)
   return (bucket_list, bucket_count)


def s3_print_bucket_list(bucket_list):
   print('\n' + 'S3 bucket cnt is ' + str(len(bucket_list)))
   for bucket in bucket_list:
      print('\t', bucket)
   print()
   return


def s3_check_bucket_in_list(s3_response, test_bucket):
   my_bucket_url = s3_response['Location']
   print('my bucket URL:  ' + my_bucket_url)
   if test_bucket in my_bucket_url:
      print(" Bucket creation passed! ")
   else:
      print(" Bucket creation failed! ")
   return


def s3_create_bucket(s3_client,NewBucket):
   s3_create_bucket_response = s3_client.create_bucket(
   Bucket = NewBucket,
   CreateBucketConfiguration={'LocationConstraint':'us-west-2'})
   return s3_create_bucket_response


def s3_delete_bucket(s3_client,OldBucket):
   s3_delete_bucket_response = s3_client.delete_bucket(Bucket = OldBucket)
   return s3_delete_bucket_response['ResponseMetadata']


def s3_check_bucket_deleteion(s3_resonse):
   if (s3_resonse['HTTPStatusCode'] == 204):
      print(" Bucket deletion passed !")
   else:
      print(" Bucket deletion failed! ")
   return


