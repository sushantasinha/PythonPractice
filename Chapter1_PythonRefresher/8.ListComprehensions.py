numbers = [1, 3, 5]
double_value = [num * 2 for num in numbers]
print(double_value)

friends = ["Rolf", "Saurav", "Sachin", "Rahul", "Sushanta"]
friends_starts_with_s = [friend for friend in friends if friend.startswith("S")]
print(friends_starts_with_s)
print("id/memory address of friends", id(friends))
print("id/memory address of friends_starts_with_s", id(friends_starts_with_s))