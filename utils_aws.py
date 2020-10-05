"""
Script containing AWS utility functions
"""
from io import BytesIO

import boto3
import botocore
import cv2
import numpy as np


def list_files(bucket, prefix):
    """Get partitions in prefix folder."""
    s3 = boto3.resource("s3")
    s3_bucket = s3.Bucket(bucket)
    return [f.key for f in s3_bucket.objects.filter(Prefix=prefix).all()]


def download_file(bucket, key, dest):
    """Download file from S3."""
    s3 = boto3.resource("s3")

    try:
        s3.Bucket(bucket).download_file(key, dest)
    except botocore.exceptions.ClientError as e:
        if e.response["Error"]["Code"] == "404":
            print("The object does not exist.")
        else:
            raise


def aws_txt_read(bucket, filename):
    """Load text file from S3."""
    s3 = boto3.resource("s3")
    obj = s3.Object(bucket, filename)
    body = obj.get()["Body"].read()
    txt = body.decode("utf-8")
    return txt


def aws_imread(bucket, blob_path):
    """Load image from S3 as array."""
    s3 = boto3.resource("s3")
    obj = s3.Object(bucket, blob_path)
    body = obj.get()["Body"].read()
    img_arr = np.asarray(bytearray(body), dtype=np.uint8)
    image = cv2.imdecode(img_arr, cv2.IMREAD_ANYCOLOR)  # BGR
    return image


def aws_buffer_read(bucket, blob_path):
    """Load file from S3 as buffer."""
    s3 = boto3.resource("s3")
    obj = s3.Object(bucket, blob_path)
    body = obj.get()["Body"].read()
    buffered = BytesIO(body)
    return buffered
