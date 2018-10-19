
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
   print()
   print("--- S3 Buckets ---")
   s3_buckets = s3_client.list_buckets()
   print(s3_buckets)
   print()
   print('s3 list_buckets() response:')
   for item in list(s3_buckets.items()):
      (key, value) = item
      print("-- ", key, ":", value)
   print()
   bucket_list = []
   bucket_count = 0
   print('s3 bucket list:')
   for bucket in s3_buckets['Buckets']:
      print('\t',bucket['Name'])
      bucket_list.append(bucket['Name'])
   print()
   bucket_count = len(bucket_list)
   return (bucket_list, bucket_count)


def s3_create_bucket(s3_client,NewBucket):
   print()
   print("--- S3 create bucket:", NewBucket, "---")
   s3_create_bucket = s3_client.create_bucket(
   Bucket = NewBucket,
   CreateBucketConfiguration={'LocationConstraint':'us-west-2'})
   print()
   print(s3_create_bucket)
   print()
   print('s3 create_buket() response:')
   for item in list(s3_create_bucket.items()):
      (key, value) = item
      print('\t', key, ":", value)
   print()
   return s3_create_bucket['Location']

def s3_delete_bucket(s3_client,OldBucket):
   print()
   print("--- S3 delete bucket:", OldBucket, "---")
   s3_delete_bucket_response = s3_client.delete_bucket(Bucket = OldBucket)
   print(s3_delete_bucket_response)
   print()
   print('s3_delete_bucket() response:')
   for item in list(s3_delete_bucket_response.items()):
      (key, value) = item
      print('\t', key, ":", value)
#  return s3_delete_bucket_response['Bucket'] 
   return 

