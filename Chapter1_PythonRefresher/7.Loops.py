user_input = input("Would you like to play (Y/n): ").lower()  #...

print("While Loop ###################################")
while user_input != "n": #...
    print("Under Input was Y. While loop repeat.")
    user_input = input("Would you like to play (Y/n): ").lower()

print("While True ###################################")
while True: #...
    print("Under Input was Y. While loop repeat.")
    user_input = input("Would you like to play (Y/n): ").lower()
    if user_input == "n":
        break #...

print("For Loop ###################################")
friends = ["one", "two", "three", "four"]
for friend in friends: #...
    print(f"{friend} is my friend")

print("For Loop with range ###################################")
for i in range(4): #...
    print(f"{i}")

print("list sum")
grades = [10, 20, 30]
print(sum(grades)) #...

numbers = [1,2,3,4,5,6,7,8,9]
events = []
for number in numbers:
    if number % 2 == 0:
        events.append(number)
print(events)

