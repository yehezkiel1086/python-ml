#!/bin/python3

import camelcase

c = camelcase.CamelCase()

lower = "hello world"

print(c.hump(lower))