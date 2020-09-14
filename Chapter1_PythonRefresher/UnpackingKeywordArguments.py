def named(**args):
    print(args)


named(name="Bob", age=25)


def named2(name, age):
    print(name)


details = {'name': 'Bob', 'age': 25}

named2(**details) # please note details MUST be a dictionary

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