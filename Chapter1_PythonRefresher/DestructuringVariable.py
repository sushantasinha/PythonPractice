x = (5, 1)
y = 5, 1
print(x)
print(y)

# So bracket is not mandatory; the bracket is needed when Python might be confused, if that is tuple or
# value inside a collection

x, y = 5, 11  # tuple de-structured or decomposed into variables
print(x)

t = 10, 20
x, y = t
print(x, y)

students_attendance = {"Rolf": 96, "Adam": 100, "Anne": 90}
print(students_attendance.items())
print(list(students_attendance.items()))  # .items() does not return a list of tuples, but something very similar

friends = [("Rolf", 24),("Adam", 30),("Anne", 20)]
for name, age in friends:
    print(name)

for name, _ in friends: # variable name can be _ but as per standard it is ignored
    print(name)

head, *tail = [1, 2, 3, 4, 5]
print(head)
print(tail)
print(*tail)

