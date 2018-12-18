
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



