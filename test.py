#!/usr/bin/env python

import sys
import urllib.request
import os
import tarfile
import subprocess

name = sys.argv[1]
download = sys.argv[2]

clear = '\033[0m'
red = '\033[31m'

print(red)
print('Hello my job name is: %s' % name)
print(clear)

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

if name == 'Job #003':
    file_name = 'coverage.tgz'
    file_path = os.path.abspath(file_name)
    urllib.request.urlretrieve('https://public-demo-files.s3.amazonaws.com/' + file_name, filename=file_name)
    coverage_path = os.path.abspath('coverage')
    if not os.path.exists(coverage_path):
        os.mkdir(coverage_path)
    tgz = tarfile.TarFile.open(file_path)
    tgz.extractall(coverage_path)
    ansible_path = os.path.abspath('ansible')
    with open('coverage/coverage=units=python-3.8.xml', 'r') as input_file:
        xml = input_file.read()
    xml = xml.replace('<source>/root/src/github.com/ansible/ansible</source>', '<source>%s</source>' % ansible_path)
    with open('coverage/coverage.xml', 'w') as output_file:
        output_file.write(xml)
    subprocess.check_output(['git', 'clone', 'https://github.com/ansible/ansible'])
    subprocess.check_output(['git', 'checkout', '022335669cc1732939cc609f8dcdc5ad75a42439'], cwd=ansible_path)
    print('Code is in: %s' % ansible_path)

if name == 'Test #001':
    print('Fail')
    sys.exit(1)  # intentional failure

print('Pass')
