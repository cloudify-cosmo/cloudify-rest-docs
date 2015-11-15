#!/bin/bash

set -e

# build
rake build

# A hack for serving the site in http://docs.getcloudify.org/api
mv build api
mkdir build
mv api build/

# push to s3
bundle exec s3_website push

