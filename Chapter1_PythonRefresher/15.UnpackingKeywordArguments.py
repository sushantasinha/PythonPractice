# ***********
# https://www.geeksforgeeks.org/args-kwargs-python/

def named(**args):
    print(args) # Output will be dictionary. so normal to dictionary if we used here.
named(name="Bob", age=25) # named param


def named1(*args):
    print(args) # Output will be tuple
named1("Bob", 25) # normal param



def named2(name, age):
    print(name)

details = {'name': 'Bob', 'age': 25}

# so dictionary to normal if we used here.
named2(**details) # please note details MUST be a dictionary


print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")


def another_method(**args):
    named(**args)
    for one, two in args.items():
        print(f"...{one}: {two}")

# If it it passing (**) then we unpacking and then sending. If ** is with method1(**args), means we are packing here
print("@@@@@@@@@@@@")
named(name="Bob", age=25)
another_method(name="Bob", age=25)



def both(*args, **kwrds): # *args collects all precitional arg; **kwrds collects all names args
    print(args)
    print(kwrds)

both(1,2,3, name="Bob", age = 25)