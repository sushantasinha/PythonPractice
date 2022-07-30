a = []
b = a

print(id(a))
print(id(b))

a.append(10)
print(a)
print(b)

print("LIST:::, as it is mutable, so it created 2 separate lists")

#...
a = []
b = []
print(id(a))
print(id(b))
#......

print("TUPLE:::, as immeutable, it create only 1 and referred from both a and b")
#...
a = ()
b = ()
print(id(a))
print(id(b))
#......

print("£££££££££££££££££")

# if we try to modify a tuple, will create a new tuple. immutable. #...

# if a integer is created it wont create another one. immutable.  #...

#...

a = 20
b = 20

print(id(a))
print(id(b))

b = 30

print(id(a))
print(id(b))
print(id(a))
print(a)
print(b)



print("£££££££££££££££££")

a = "Hello"
b = a
a += " World"

print(a)
print(b)

print("£££££££££££££££££")

#......

# -----------------------------------------

from typing import List


class Student:
    def __init__(self, name: str, grades: List[int] = []):  # this is bad. Never use mutable value as default vale
        self.name = name
        self.grades = grades

    def take_exam(self, result: int):
        self.grades.append(result)


bob = Student("Bob")
rolf = Student("Rolf")

bob.take_exam(90)
print(bob.grades)
print(rolf.grades)  # Rolf got rating even if he did not take exam!!!


# Reason: grade will be assigned in __init__ when the function is defined not when the function is called so,
# for both object we assigned [] (default value) list which is mutable
# but there won't be any issues if we pass grede value as well instead of using default one or use as below:


#Or we can use OPTIONAL here

class StudentAnother:
    def __init__(self, name: str, grades=None):  # this is bad. Never use mutable value as default value
        if grades is None:
            grades = []  # or self.grades = grades or []
        self.name = name
        self.grades = grades

    def take_exam(self, result: int):
        self.grades.append(result)


bob = StudentAnother("Bob")
rolf = StudentAnother("Rolf")

bob.take_exam(90)
print(bob.grades)
print(rolf.grades)
