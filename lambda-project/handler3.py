import csv
import json
import boto3
import pandas as pd
import os
import glob

# def lambda_handler(event, context):

#Creates boto3 s3 session that is connected to localstack
s3 = boto3.resource('s3', aws_access_key_id="123", aws_secret_access_key="124", endpoint_url="http://s3.localhost.localstack.cloud:4566")
session = boto3.client("s3", endpoint_url="http://s3.localhost.localstack.cloud:4566/", region_name='us-east-1')

bucket_name = 'bucket_em'

#creates bucket
session.create_bucket(Bucket=bucket_name)

#Reads from CSV file
files = os.path.join("example*.csv")
files = glob.glob(files)
df = pd.concat(map(pd.read_csv, files), ignore_index=True)
df.to_json('Colors.json')

#Creates json file and puts it in the bucket
with open ("Colors.json", "w") as f:
    s3object = s3.Object("bucket_em", "Colors.json")

    s3object.put(Body=(bytes(json.dumps("Colors.json").encode("UTF-8"))))