import boto3

BUCKET_NAME = "student-performance-ml-bucket"

s3 = boto3.client("s3")

response = s3.list_objects_v2(Bucket=BUCKET_NAME)

print("S3 Connected Successfully!")

if "Contents" in response:
    for obj in response["Contents"]:
        print(obj["Key"])
else:
    print("Bucket is empty")