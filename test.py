#!/usr/bin/env python

import sys

name = sys.argv[1]

print('Hello my job name is: %s' % name)

if name == 'T001':
    print('Fail')
    sys.exit(1)

print('Pass')
