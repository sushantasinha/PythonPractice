from mymodule import divide

# Need folder in relative import
# operator.py lib.operations.operator
# mylib.py lib.mylib
# MyModule.py mymodule
# RelativeImport.py __main__
# Also, need to use from .. import ..
# SO for relative import need sub directory


print("RelativeImport.py", __name__)
print(divide(10, 2))

