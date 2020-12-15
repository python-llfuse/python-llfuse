#!/bin/sh

set -e

pip install pytest pytest-catchlog cython sphinx
cython --version
