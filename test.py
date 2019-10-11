#!/usr/bin/env python

import sys
import urllib.request
import os
import tarfile

name = sys.argv[1]
download = sys.argv[2]

print('Hello my job name is: %s' % name)

if download:
    file_name = '%s.tgz' % download
    file_path = os.path.abspath(file_name)
    url = 'https://public-demo-files.s3.amazonaws.com/' + file_name
    print('Downloading: %s' % url)
    urllib.request.urlretrieve(url, filename=file_name)
    print('Download complete: %s' % file_path)
    result_path = os.path.abspath('results')
    if not os.path.exists(result_path):
        os.mkdir(result_path)
    tgz = tarfile.TarFile.open(file_path)
    tgz.extractall(result_path)


if name == 'Test #001':
    print('Fail')
    sys.exit(1)  # intentional failure

print('Pass')
