#!/usr/bin/env python

import sys

name = sys.argv[1]

print('Hello my job name is: %s' % name)

if name == 'Two':
    print('Fail')
    sys.exit(1)

if name == 'Three':
    print('Fail')
    sys.exit(1)

if name == 'Four':
    print('Fail')
    sys.exit(1)

print('Pass')
