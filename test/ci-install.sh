#!/bin/sh

set -e

pip install pytest cython "sphinx<7.0"
cython --version
