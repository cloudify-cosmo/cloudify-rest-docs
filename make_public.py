
#####
# A script for making rest api docs s3 bucket keys public.

import os

import boto
from boto.s3.connection import S3Connection


def make_api_docs_public():
    # from some reason /api keys are not public after pushed to s3.
    # Therefore, it is done manually using boto.
    print('-- Making api docs S3 bucket keys public...')
    conn = S3Connection(
        os.environ['S3_ACCESS_KEY_ID'],
        os.environ['S3_SECRET_KEY'],
        calling_format=boto.s3.connection.OrdinaryCallingFormat())
    bucket = conn.get_bucket('docs.getcloudify.org')
    api_keys = bucket.list(prefix='api/v2/')
    for key in api_keys:
        print('   Making "{0}" public..'.format(key.name))
        key.make_public()
    print('-- Done!')


if __name__ == '__main__':
    make_api_docs_public()
