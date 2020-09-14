users = [
    (9, "Bob", "pass123"),
    (9, "Sachin", "pass1234"),
    (9, "Pat", "pass123456")
]

username_mapping = {user[1]: user for user in users}
print(username_mapping["Bob"])