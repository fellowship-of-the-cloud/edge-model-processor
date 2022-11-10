# This is a sample Python script.

# Press Mayús+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


import boto3


ACCESS_KEY = 'AKIAT4EI2IX2VVOCQBOV'
SECRET_KEY = 'bfbYbkWtkF6H1X9q2IE7l2y1FZheZgW/RyFlPhUw'
FILE_NAME = 'dataset_20221109174337.csv'
BUCKET_NAME = 'hackaton-team-the-fellowship-of-the-cloud'
OBJECT_NAME = 'MVP3/dataset_20221109174337.csv'

s3 = boto3.client('s3', aws_access_key_id='AKIAT4EI2IX2VVOCQBOV', aws_secret_access_key='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')
with open(FILE_NAME, 'wb') as f:
    s3.download_fileobj(BUCKET_NAME, OBJECT_NAME, f)
    print(open(FILE_NAME).read())
