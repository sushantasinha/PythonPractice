users = [
    (9, "Bob", "pass123"),
    (9, "Sachin", "pass1234"),
    (9, "Pat", "pass123456")
]

username_mapping = {user[1]: user for user in users} # user[1] = key = Bob/...  abd uer obj is value
print(username_mapping["Bob"])
print(username_mapping["Sachin"][2])