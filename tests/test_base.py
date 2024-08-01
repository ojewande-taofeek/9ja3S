#!/usr/bin/python3

from seniors.base_seniors import BaseSenior

Base = BaseSenior()

print(Base)
base_json = Base.to_dict()
print(type(base_json))
print(type(base_json))
print("Base JSON:")
for key, value in base_json.items():
    print("{}: {}".format(key, value))

new_base = BaseSenior(**base_json)
print("New Base:")
print(type(new_base))
print(type(new_base.created_at))
new_base.save()
print(new_base.to_dict())

