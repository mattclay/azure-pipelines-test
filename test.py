#!/usr/bin/env python

import sys
import random

name = sys.argv[1]

print('Hello my job name is: %s' % name)

if name == 'Job #002':
    print('Job "%s" should not run.')
    sys.exit(1)

if random.randint(1, 3) == 1:
    print('Fail')
    sys.exit(1)  # intentional failure

print('Pass')
