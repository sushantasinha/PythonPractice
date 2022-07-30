#...
# 1

print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")
def multiply(*args):
    print(args)
    total = 1
    for arg in args:
        total = total * arg
    return total

print(multiply(1, 3, 5))



# 2
print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")
def add(x, y):
    return x + y

nums = [3, 5] # need same number of arg (i.e. 2 arg for x and y)
print(add(*nums)) # destructure and map x and y



# 3
print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")
def print_another(x, y):
    print(f"x: {x} y: {y}")

nums = {"y": 10, "x": 5} # dictionary
print_another(**nums)  # passing as names arg i.e. x  mapped with x present in print_another x and same for y


# 4
print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")
def multiply_another(args):
    print(args)
    total = 1
    for arg in args:
        total = total * arg
    return total

def apply(*args, operator):
    if operator == "*":
        print(f"@@@@@@@@@@@@@@@@@@@@@ {args}");
        print(f":::::::::::{multiply_another(args)}")
        return multiply(*args)
        # return multiply(*args) try this
    elif operator == "+":
        # print(args)
        return sum(args)
    else:
        return "Invalid operator"


print(apply(1, 2, 3, 4, operator="+"))
# print(apply(1, 2, 3, 4, "+")) Error

print(":::")
print(apply(1, 2, 3, 4, operator="*"))

