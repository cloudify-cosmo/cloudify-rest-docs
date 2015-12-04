
Cloudify REST API Docs
======================

Cloudify's REST API documentation is based on [Slate](https://github.com/tripit/slate).

The documentation is available at [api.getcloudify.org](http://docs.getcloudify.org/api).

[![Circle CI](https://circleci.com/gh/cloudify-cosmo/cloudify-rest-docs.svg?style=svg)](https://circleci.com/gh/cloudify-cosmo/cloudify-rest-docs)

# Installation

* Clone this repository.
* Make sure you have `ruby` in your path with `bundler` installed (gem install bundler).
* Install ruby-dev
* Run `bundler install` for installing the necessary dependencies.

# Running A Local Server

Run: `bundle exec middleman server`

The documentation will be available at: http://localhost:4567/

The middleman server is automatically watching for changes.
