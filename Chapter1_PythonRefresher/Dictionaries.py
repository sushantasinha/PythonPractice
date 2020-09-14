friend_args = {"Rolf": 24}  # Dictionary of single element
friend_args = {"Rolf": 24, "Adam": 30}
print(friend_args["Adam"])
friend_args["Adam"] = 40
print(friend_args["Adam"])
print(friend_args)

# Another Dictionary
friends = [
    {"name": "Rolf", "age": 24},
    {"name": "Adam", "age": 30},
    {"name": "Anne", "age": 20}
]
print(friends[1]["name"])

# Another Dictionary
students_attendance = {"Rolf": 96, "Adam": 100, "Anne": 90}
print("For loop 1:")
for student in students_attendance:
    print(f"{student}: {students_attendance[student]}")
print("For loop 2:")
for student, attendance in students_attendance.items():
    print(f"{student}: {attendance}")

if "Rolf" in students_attendance:
    print("Rolf is a student")
else:
    print("Rolf is NOT a students")

print("avg:", sum(students_attendance.values()) / len(students_attendance))

