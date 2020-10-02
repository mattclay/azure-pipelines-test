#!/usr/bin/env python

import sys
import random

name = sys.argv[1]

print('Hello my job name is: %s' % name)

value = random.randint(1, 3)

if value == 1:
    print('Fail: %s' % value)
    sys.exit(1)  # intentional failure

print('Pass')
