x = (5, 1)
y = 5, 1
print(x)
print(y)

# So bracket is not mandatory; the bracket is needed when Python might be confused, if that is tuple or
# value inside a collection
# x = [(5,11)] -> a list, inside which i tuple


x, y = 5, 11  # tuple de-structured or decomposed into variables #...
print(x)

t = 10, 20
x, y = t
print(x, y)

students_attendance = {"Rolf": 96, "Adam": 100, "Anne": 90}
print(":::::::::::::::::")
print(students_attendance.items())
print(list(students_attendance.items()))  # .items() does not return a list of tuples, but something very similar #...

friends = [("Rolf", 24),("Adam", 30),("Anne", 20)]
for name, age in friends:
    print(name)


print("@@@@@@: similar like above; but the above approach is much more readable")
for person in friends:
    print(f"Name: {person[0]} and grade: {person[1]}")

for name, _ in friends: # variable name can be _ but as per standard, we define a variable name as _ if we meant this to be ignored
    print(name)

print("::::::::::::::::::::::::::::::::::")

#...
head, *tail = [1, 2, 3, 4, 5]
print(head)
print(tail)
print(*tail)
#......
