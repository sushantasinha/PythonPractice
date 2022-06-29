# This file will be imported to 20.1.Import.py

import lib.mylib

# Below are valid
# import lib.operations.operator
# from lib.operations import operator

def divide(divident, divisor):
    return divident / divisor


# __name__ will help us to distinguish the file we run and the file we import
print("MyModule.py", __name__)
