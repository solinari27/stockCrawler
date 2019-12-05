#!usr/bin/env python
# -*- coding:utf-8 _*-
"""
@author: solinari
@file: pull_mongo.py
@time: 2019/04/27
"""
import os
import tarfile
import datetime
from boto3.session import Session
import boto3


MONGO_DUMP = "/home/solinari/mongodump"
TAR_FILE = "/tmp/tartest.tar.gz"
ACCESS_KEY = 'AKIAJUL5J2M422GJ26QQ'
SECRET_KEY = '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'
BUCKET = 'stockcrawler'
REGION = 'ap-northeast-2'
RETRY_TIME = 50


# def make_tar():
#     tar = tarfile.open(TAR_FILE, "w:gz")
#
#     for root, dir, files in os.walk(MONGO_DUMP):
#         for file in files:
#             fullpath = os.path.join(root, file)
#             tar.add(fullpath)
#     tar.close()


def s3_download():
    session = Session(aws_access_key_id=ACCESS_KEY,
                      aws_secret_access_key=SECRET_KEY,
                      region_name=REGION)
    s3 = session.resource('s3')
    client = session.client('s3')

    # upload_data = open(TAR_FILE, 'rb')
    # s3.Bucket(BUCKET).get_object(Key=upload_file, Body=upload_data)
    # client.download_file(Bucket=BUCKET, Key=upload_file, '/tmp/download_file.tar.gz')
    bucket_info = client.list_objects(Bucket=BUCKET)
    # print bucket_info
    # for item in bucket_info:
    #     print item, bucket_info[item]
    file = bucket_info['Contents'][0]['Key']
    day = bucket_info['Contents'][0]['LastModified']
    counts = len(bucket_info['Contents'])
    for i in range(0, counts):
        if bucket_info['Contents'][i]['LastModified'] > day:
            file = bucket_info['Contents'][i]['Key']
            day = bucket_info['Contents'][i]['LastModified']

    print ('start to download file %s form AWS S3.', file)
    client.download_file(BUCKET, file, '/home/mongo_backup.tar.gz')
    print ('download finished.')

# main
# make_tar()
# today = datetime.datetime.today().strftime('%Y_%m_%d')
# filename = "mongodump_" + today
# for i in range(0, RETRY_TIME):
#     try:
#         s3_upload(upload_file=filename)
#         break
#     except:
#         continue

s3_download()
