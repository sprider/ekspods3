import os
import datetime
import boto3
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

def upload_file_to_s3(bucket_name, file_name):
    if not bucket_name:
        print("Bucket name is not set")
        return
    s3_client = boto3.client("s3")
    try:
        s3_client.upload_file(file_name, bucket_name, file_name)
    except Exception as e:
        print(f"Error: {e}")

# Get the aws s3 bucket name from environment variables 
bucket = os.environ.get("AWS_S3_BUCKET_NAME")

# Check if bucket name is set
if not bucket:
    print("AWS_S3_BUCKET_NAME environment variable is not set.")
else:
    # Get the current time
    current_time = datetime.datetime.now()
    # Format the time into a string. For example: '2024-01-22_15-30-25'
    formatted_time = current_time.strftime("%Y-%m-%d_%H-%M-%S")
    # Create a file name with the formatted time
    file_to_upload = f"example_{formatted_time}.txt"

    # Write a sample file
    with open(file_to_upload, "w") as file:
        file.write("This is a sample file for S3")

    # Upload the file
    upload_file_to_s3(bucket, file_to_upload)
