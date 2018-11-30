city = ('London', 'Delhi', 'Boston', 'Sydeny')
 city = ('London', 'Delhi', 'Boston', 'Sydeny')
>>> city
('London', 'Delhi', 'Boston', 'Sydeny')
>>> city[2]
'Boston'
>>> city[2]='Helsinki'
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: 'tuple' object does not support item assignment
>>> city
('London', 'Delhi', 'Boston', 'Sydeny')
>>> len(city)
4
>>> del city
>>> city
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'city' is not defined


##Dictionaries
animal = {
    "breed": "pug",
    "type": "dog",
    "color": "mud"
}

animal = {
...     "breed": "pug",
...     "type": "dog",
...     "color": "mud"
... }
>>> animal
{'color': 'mud', 'breed': 'pug', 'type': 'dog'}
>>> animal['type']
'dog'
>>> animal['color']
'mud'
>>> animal.get['color']
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: 'builtin_function_or_method' object has no attribute '__getitem__'
>>> color = animal.get['color']
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: 'builtin_function_or_method' object has no attribute '__getitem__'
>>> color = animal.get('color')
>>> color
'mud'
>>> animal['color']="green"
>>> animal
{'color': 'green', 'breed': 'pug', 'type': 'dog'}
>>> animal['weight']=56
>>> animal
{'color': 'green', 'breed': 'pug', 'type': 'dog', 'weight': 56}
>>> len(animal)
4
>>> animal.pop('type')
'dog'
>>> animal
{'color': 'green', 'breed': 'pug', 'weight': 56}
>>> del animal['colo']
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
KeyError: 'colo'
>>> del animal['color']
>>> animal
{'breed': 'pug', 'weight': 56}
>>> animal.clear()
>>> animal
{}
>>> 
