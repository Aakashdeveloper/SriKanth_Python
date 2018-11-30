cars = "Bmw, Volvo, Merc"
cars = "Bmw, Volvo, Merc"
>>> cars
'Bmw, Volvo, Merc'
>>> cars.split(',')
['Bmw', ' Volvo', ' Merc']
>>> output = cars.split(',')
>>> output
['Bmw', ' Volvo', ' Merc']
>>> output[0]
'Bmw'
>>> output[1]
' Volvo'
>>> output[2]
' Merc'
>>> output[3]
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
IndexError: list index out of range
>>> weather = 'https://www.bbc.co.uk/weather/2650225'
>>> weather.split('/')
['https:', '', 'www.bbc.co.uk', 'weather', '2650225']
>>> out = weather.split('/')
>>> out.len()
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
AttributeError: 'list' object has no attribute 'len'
>>> out.length()
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
AttributeError: 'list' object has no attribute 'length'
>>> out
['https:', '', 'www.bbc.co.uk', 'weather', '2650225']
>>> out[4]
'2650225'
>>>  weather = 'https://www.bbc.co.uk/weather/j/2650225'
  File "<stdin>", line 1
    weather = 'https://www.bbc.co.uk/weather/j/2650225'
    ^
IndentationError: unexpected indent
>>> weather = 'https://www.bbc.co.uk/weather/j/2650225'
>>> out = weather.split('/')
>>> out
['https:', '', 'www.bbc.co.uk', 'weather', 'j', '2650225']
>>> len(out)
6
>>> out[6]
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
IndexError: list index out of range
>>> out[len(out)-1]
'2650225'
>>> out[len(out)-1]



cars = ["BMW","MERC", "VOLVO", "KIA"]

for data in cars:
    print(data)

age = 20
if age<18:
    print("you can vote")
elif age ==21:
    print("prefect age to vote")
else:
    print("you cannot vote")

classname= "python"
topic = "machine learning"

"I am doing {0} for {1}".format(classname, topic)


classname= "python"
topic = "machine learning"
"i am doing " + classname+ " for " +topic

a = 10
b = 20

if a > b :print("a is greater")


a = 10
b = 20

min = a if a < b else b
print min

a = 10
b = 20

out = "hii" if a > b else "bie"
print out

number = 5
if number:
    print("number is 5")

number = 6 
if number !=5:
    print("number will work")

null / None

word = None
if word:
    print("hiii")

word = False
if not word:
    print("okkkk")