# This file will be imported to Import.py

import lib.mylib

# Below ate valid
# import lib.operations.operator
# from lib.operations import operator

def divide(divident, divisor):
    return divident / divisor


# __name__ will help us to distinguish he file we run and the file we import
print("MyModule.py", __name__)
