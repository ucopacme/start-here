def s3_print_bucket_list(bucket_list):
   print('\n' + 'S3 bucket cnt is ' + str(len(bucket_list)))
   for bucket in bucket_list:
      print('\t', bucket)
   print()
   return

def s3_check_bucket_deleteion(s3_resonse):
   if (s3_resonse['HTTPStatusCode'] == 204):
      print(" Bucket deletion passed !")
   else:
      print(" Bucket deletion failed! ")
   return

