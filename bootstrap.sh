#!/usr/bin/env bash

# Python
apt-get update
apt-get install -y python-pip
pip install virtualenv
cd /vagrant && virtualenv .env && cd ~
