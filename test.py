#!/usr/bin/env python

import sys
import time

name = sys.argv[1]

print('Hello my job name is: %s' % name)

for i in range(1, 10):
    print('Sleeping for %d second(s)' % i)
    time.sleep(i)

if name == 'Test #001':
    print('Fail')
    sys.exit(1)

print('Pass')
