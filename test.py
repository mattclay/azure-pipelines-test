#!/usr/bin/env python

import sys
import random

name = sys.argv[1]

print('Hello my job name is: %s' % name)

if random.randint(1, 3) == 1:
    print('Fail')
    sys.exit(1)  # intentional failure

print('Pass')
