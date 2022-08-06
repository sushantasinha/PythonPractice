def get_admin_password():
    return "1234"


def make_secure(func):
    def secure_function():
        if user["access_level"] == "admin":
            return func()
        else:
            return f"No admin permissions for {user['username']}."

    return secure_function


get_admin_password = make_secure(
    get_admin_password
)  # `get_admin_password` is now `secure_func` from above

user = {"username": "jose", "access_level": "guest"}
print(get_admin_password())  # Now we check access level

user = {"username": "bob", "access_level": "admin"}
print(get_admin_password())  # Now we check access level

#... $$$$$$
"""
Decorators are a very powerful and useful tool in Python since it allows programmers to modify the behaviour of a function or class. 
Decorators allow us to wrap another function in order to extend the behaviour of the wrapped function, without permanently modifying it. 

i.e. A decorator takes in a function, adds some functionality and returns it.
"""
#......
