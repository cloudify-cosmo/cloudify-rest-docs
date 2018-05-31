
Cloudify REST API Docs
======================

Cloudify's REST API documentation is built with [Hugo](https://gohugo.io/) and is based on the [DocuAPI](https://github.com/bep/docuapi) theme and [Slate](https://github.com/tripit/slate).

The documentation is available in the [Cloudify Documentation Center](https://docs.cloudify.co/latest/developer/apis/rest-service/).

[![CircleCI](https://circleci.com/gh/cloudify-cosmo/cloudify-rest-docs/tree/master.svg?style=shield)](https://circleci.com/gh/cloudify-cosmo/cloudify-rest-docs/tree/master)

# Installing the Cloudify Documentation Center

To run the Cloudify Documentation Center locally:

1. Install the latest Hugo:

    * On CentOS:

        1. Install the copr plugin for yum: `sudo yum install yum-plugin-copr`
        1. Enable the Hugo repository: `sudo yum copr enable daftaupe/hugo`
        1. Install Hugo: `sudo yum install hugo`

    * On Ubuntu:
    
        * Install Hugo: `sudo apt-get install hugo`

    * On Windows:

        1. Install [chocolatey](https://chocolatey.org/install).
        1. Install Hugo: `choco install hugo -confirm`
        
    * On MacOS:

        1. Install [homebrew](https://brew.sh/)
        2. Install Hugo: `brew install hugo`

1. Verify that Hugo is installed: `hugo version`
1. Clone this repository to your local host.
1. Change directory to the cloudify-rest-docs directory.
1. Start the hugo web server: `hugo server`

To access the site, go to: http://localhost:1313
