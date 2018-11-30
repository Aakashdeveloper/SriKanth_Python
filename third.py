list [] is more similiar to like array, in this data changeable and duplicate value can be inserted 
set {} you cannot have duplicate record, data is unordered and unindexed
tuple () you can have duplicate record but its unchangeable
dictionary {object }no cannot have duplicate member changeable and indexed

#List

cars = ["BMW", "AUDI","KIA"]
cars = ["BMW", "AUDI","KIA"]
>>> print(cars)
['BMW', 'AUDI', 'KIA']
>>> cars[1]
'AUDI'
>>> cars[0]
'BMW'
>>> cars[1]="volvo"
>>> cars
['BMW', 'volvo', 'KIA']
>>> len(cars)
3
>>> cars.append('audi')
>>> cars
['BMW', 'volvo', 'KIA', 'audi']
>>> cars.remove('kia')
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ValueError: list.remove(x): x not in list
>>> cars.remove('KIA')
>>> cars
['BMW', 'volvo', 'audi']
>>> cars.pop()
'audi'
>>> cars
['BMW', 'volvo']
>>> cars.append('audi')
>>> cars.append('kia')
>>> cars
['BMW', 'volvo', 'audi', 'kia']
>>> cars.pop(2)
'audi'
>>> cars.pop()
'kia'
>>> cars.append('kia')
>>> cars.append('kia')
>>> cars.append('audi')
>>> cars
['BMW', 'volvo', 'kia', 'kia', 'audi']
>>> cars.pop(3)
'kia'
>>> cars
['BMW', 'volvo', 'kia', 'audi']
>>> cars.pop()
'audi'
>>> cars.pop(-1)
'kia'
>>> cars.append('audi')
>>> cars.append('kia')
>>> cars
['BMW', 'volvo', 'audi', 'kia']
>>> cars.insert(2,"merc")
>>> cars
['BMW', 'volvo', 'merc', 'audi', 'kia']
>>> del cars[1]
>>> cars
['BMW', 'merc', 'audi', 'kia']
>>> cars.sort()
>>> cars
['BMW', 'audi', 'kia', 'merc']
>>> cars1 = cars.sort()
>>> cars1
>>> cars.sort()
>>> cars
['BMW', 'audi', 'kia', 'merc']
>>> cars.sort()
>>> print(cars.sort()
... )
None
>>> del cars[0]
>>> cars
['audi', 'kia', 'merc']
>>> cars.append('bmw')
>>> cars
['audi', 'kia', 'merc', 'bmw']
>>> cars.sort()
>>> 
