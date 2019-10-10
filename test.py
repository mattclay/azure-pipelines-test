#!/usr/bin/env python

import sys

name = sys.argv[1]

print('Hello my job name is: %s' % name)

if name == 'Test #001':
    print('Fail')
    sys.exit(1)  # intentional failure

print('Pass')
