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
var_value = json.dumps(config)

# see https://docs.microsoft.com/en-us/azure/devops/pipelines/scripts/logging-commands?view=azure-devops&tabs=bash
print('Setting variable: %s' % var_name)
print('##vso[task.setVariable variable=%s;isOutput=true]%s' % (var_name, var_value))
print('Variable has been set to: %s' % var_value)
