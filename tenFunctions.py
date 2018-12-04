>>> a = "srikanth"
>>> a.title()
'Srikanth'
>>> a = "srikanth python"
>>> a.title()
'Srikanth Python'
>>> a.upper()
'SRIKANTH PYTHON'
>>> a.lower()
'srikanth python'

students = []

def add_student(name,rollno):
    student = {"name":name, "rollno":rollno}
    students.append(student)

 def get_students():
    student_titleCase = [ ]
    for stud in students:
        student_titleCase.append(stud['name'].title())
    print(student_titleCase)    

students = []
def add_only_name(name):
    student = name
    students.append(student)

def get_students():
    student_titleCase = [ ]
    for stud in students:
        student_titleCase.append(stud.title())
    print(student_titleCase) 


def with_normal(name, classname):
    print(name)
    print(classname)

def with_args(name, *args):
    print(name)
    print(args)

def with_keyvalue(name, **kwargs):
    print(name)
    print(kwargs)