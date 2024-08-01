#!/usr/bin/python3

from seniors.base_seniors import BaseSenior
from seniors import storage


all_objs = storage.all()
print("-- Reloaded objects --")
for obj_id in all_objs.keys():
    obj = all_objs[obj_id]
    print(obj)

print("-- Create a new object --")
my_model = BaseSenior()
my_model.name = "My_First_Model"
my_model.my_number = 89
my_model.save()
print(my_model)