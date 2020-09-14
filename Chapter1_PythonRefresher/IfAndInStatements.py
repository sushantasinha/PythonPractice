day_of_week = input("Enter Day: ").lower()

if day_of_week == "monday":
    print("Have a great start of the week")
elif day_of_week == "tuesday":
    print("It's Tuesday")
else:
    print("Full speed ahead")

friends = ["Friend1", "Friend2", "Friend3"]
print("Friend2" in friends)

user_input = input("Enter Friend name: ").lower()
if user_input in friends:
    print(f"{user_input} is in my friend list too!")
else:
    print(f"{user_input} is NOT in my friend list")

if user_input in ("friend1", "friend2"):
    print("Input was Friend1 or Friend2")




