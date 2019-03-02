#!usr/bin/env python
# -*- coding:utf-8 _*-
"""
@author: solinari
@file: tests3.py
@time: 2019/03/02
"""
from boto3.session import Session
import boto3

# aws_access_key_id = config.get('s3_credentials', 'aws_access_key_id')
# aws_secret_access_key = config.get('s3_credentials','aws_secret_access_key')
# bucket = config.get('s3_credentials', 'bucket')
# region = config.get('s3_credentials', 'region')
aws_access_key_id = 'AKIAJUL5J2M422GJ26QQ'
aws_secret_access_key = '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'
bucket = 'stockcrawler'
region = 'ap-northeast-2'

# session = Session(aws_access_key_id=aws_access_key_id, aws_secret_access_key=aws_secret_access_key, region_name=region)
# client = session.client('s3')

session = Session(aws_access_key_id=aws_access_key_id,
                  aws_secret_access_key=aws_secret_access_key,
                  region_name=region)  # 此处根据自己的 s3 地区位置改变
s3 = session.resource('s3')
client = session.client('s3')
bucket = 'stockcrawler'  # 【你 bucket 的名字】 # 首先需要保证 s3 上已经存在该存储桶，否则报错
# print s3.Bucket(bucket).list()



# s3_client = boto3.client('s3', endpoint_url=None,
#                          aws_access_key_id=aws_access_key_id,
#                          aws_secret_access_key=aws_secret_access_key,
#                          region_name=region)

upload_data = open("/home/solinari/ec2.pem", 'rb')
upload_key = "test"
file_obj = s3.Bucket(bucket).put_object(Key=upload_key, Body=upload_data)
print(file_obj)


# def is_s3_file_exist(key):
#     '''
#      weather s3 exists this key
#      return True exist
#     '''
#     bucket_name = 'stockcrawler'
#     # connect to the bucket
#     conn = boto.connect_s3('',
#                     AWS_SECRET_ACCESS_KEY)
#     bucket = conn.get_bucket(bucket_name)
#
#     # create a key to keep track of our file in the storage
#     k = Key(bucket)
#     k.key = key
#
#     if k.exists(None):
#         logging.info("s3 exists this file")
#         return True
#     else:
#         return False
