
import boto3


s3 = boto3.client('s3')
with open("parking_json", "rb") as f:
    s3.upload_fileobj(f, "Manoj_S3_bucket", "media/user/data")