#!/bin/sh

set -e

# as long as we test on python 3.4, we need pytest < 5.0
pip install 'pytest<5.0' pytest-catchlog cython sphinx
cython --version
