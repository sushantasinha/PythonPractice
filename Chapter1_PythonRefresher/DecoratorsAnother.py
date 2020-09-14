import functools

def make_secure(func): # This is decorator
    @functools.wraps(func) # keeps the documentation of internal method which is Not registered which is  get_admin_password()
    def secure_function():
        if user["access_level"] == "admin":
            return func()
        else:
            return f"No admin permissions for {user['username']}."

    return secure_function


@make_secure
def get_admin_password():
    return "1234"


user = {"username": "jose", "access_level": "guest"}
print(get_admin_password())  # Now we check access level

user = {"username": "bob", "access_level": "admin"}
print(get_admin_password())  # Now we check access level

print(get_admin_password.__name__) # Run this with and without @functools.wraps(func)