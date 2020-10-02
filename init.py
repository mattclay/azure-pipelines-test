#!/usr/bin/env python

import json

var_name = 'config'
config = dict()

for job in range(1, 10 + 1):
    key = 'J%03d' % job
    config[key] = dict(
        name='Job #%03d' % job,
    )

var_value = json.dumps(config, sort_keys=True)

# see https://docs.microsoft.com/en-us/azure/devops/pipelines/scripts/logging-commands?view=azure-devops&tabs=bash
print('Setting variable: %s' % var_name)
print('##vso[task.setVariable variable=%s;isOutput=true]%s' % (var_name, var_value))
print('Variable has been set to: %s' % var_value)

# comment
