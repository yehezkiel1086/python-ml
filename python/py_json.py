#!/bin/python3

import json

person_json = '{"name": "Ben", "age": 23, "city": "Tokyo"}'
car = {
  "name": "Supra MKIV",
  "manufacturer": "Toyota",
  "year": 2000
}

# json to python
person = json.loads(person_json)

# python to json
car_json = json.dumps(car)

print(person["name"])
print(car_json)