import json

person1 =  '{ "name":"John", "age":30, "city":"New York"}'

y = json.loads(person1)

print(y)