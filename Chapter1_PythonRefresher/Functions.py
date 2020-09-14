def hello():
    print("Hello!")


hello()

# Valid code but wont work as like 9 will call line 8
# def print():
#    print("...")
# print()

friends = ["Rob", "Bob"]


def add_friend():
    another_friend = "Sachin"
    # will work
    # f = friends + [another_friend]
    # print(friends)

    # But friends = friends + [another_friend] won't work. to get this worked:global friends
    global friends
    friends = friends + [another_friend]
    print(friends)


add_friend()


def print_response(x, y):
    print(f"Result: {x} {y}")


print_response("Hello", "World!")
print_response(y="World", x="Hello")


def print_response_default(x, y="World..."):
    print(f"Result: {x} {y}")


print_response_default("Hello")

# Default param value must be at end after non default value i.e print_response_default(x= 5, y) won't work

default_y = 3


def add(x, y=default_y):
    print(f":::{x} and {y}")


add(2)
default_y = 4
add(2)  # default_y wont change after set that to function


# Note: None is a special value in Python: no value, special value

def add_return(x, y, z):
    return x + y + z


print(add_return(1, 2, 3))
# Just return without a value will npt return anything


