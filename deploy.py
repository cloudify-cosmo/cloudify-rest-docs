
import os
import shutil

import boto
from boto.s3.connection import S3Connection


def build_docs():
    print('-- Building REST API docs...')
    if os.system('rake build') != 0:
        raise RuntimeError('rake build failed')


def create_api_dir():
    print('-- Moving build to build/api...')
    shutil.move('build', 'api')
    os.makedirs('build')
    shutil.move('api', 'build/api')


def push_docs_to_s3():
    print('-- Pushing generated docs to S3...')
    if os.system('bundle exec s3_website push --verbose') != 0:
        raise RuntimeError('s3_website push failed')


def set_docs_public():
    # from some reason /api keys are not public after pushed to s3.
    # Therefore, it is done manually using boto.
    print('-- Making docs S3 bucket keys public...')
    conn = S3Connection(
        os.environ['S3_ACCESS_KEY_ID'],
        os.environ['S3_SECRET_KEY'],
        calling_format=boto.s3.connection.OrdinaryCallingFormat())
    bucket = conn.get_bucket('docs.getcloudify.org')
    api_keys = bucket.get_all_keys(prefix='api')
    for key in api_keys:
        print('   Making "{0}" public..'.format(key.name))
        key.make_public()


if __name__ == '__main__':
    # build_docs()
    # create_api_dir()
    # push_docs_to_s3()
    set_docs_public()
    print('-- Done!')
