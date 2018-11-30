brands = {'Samsung', 'apple', 'lg'}
>>> brands
set(['lg', 'apple', 'Samsung'])
>>> brands[1]
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: 'set' object does not support indexing
>>> brands.add('oppo')
>>> brands
set(['lg', 'apple', 'oppo', 'Samsung'])
>>> brands.update(['vivo','mi'])
>>> brands
set(['lg', 'apple', 'Samsung', 'mi', 'vivo', 'oppo'])
>>> len(brands)
6
>>> brands
set(['lg', 'apple', 'Samsung', 'mi', 'vivo', 'oppo'])
>>> brands.add('oppo')
>>> barnds
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'barnds' is not defined
>>> brands
set(['lg', 'apple', 'Samsung', 'mi', 'vivo', 'oppo'])
>>> brands.pop()
'lg'
>>> brands.pop()
'apple'
>>> brands.pop()
'Samsung'
>>> brands.pop(4)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: pop() takes no arguments (1 given)
>>> brands.clear()
>>> brands
set([])
>>> 
