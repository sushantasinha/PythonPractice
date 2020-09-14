import functools

def make_secure(func):
    @functools.wraps(func)
    def secure_function(*arg, **kwargs): # If we pass panel param: will work; but used "*arg, **kwargs" to make it generic and work with others
        if user["access_level"] == "admin":
            return func(*arg, **kwargs)
        else:
            return f"No admin permissions for {user['username']}."

    return secure_function


@make_secure
def get_password(panel):
    if panel == "admin":
        return "1234"
    elif panel == "billing":
        return "super_secured_password"


user = {"username": "jose", "access_level": "guest"}
print(get_password("billing"))  # Now we check access level

user = {"username": "bob", "access_level": "admin"}
print(get_password("billing"))  # Now we check access level
