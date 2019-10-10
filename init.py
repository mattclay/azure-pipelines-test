#!/usr/bin/env python

import json

var_name = 'config'
config = dict(
    a=dict(
        name='A',
    ),
    b=dict(
        name='B',
    ),
)

# see https://docs.microsoft.com/en-us/azure/devops/pipelines/scripts/logging-commands?view=azure-devops&tabs=bash
print('##vso[task.setVariable variable=%s;isOutput=true]%s' % (var_name, json.dumps(config)))
