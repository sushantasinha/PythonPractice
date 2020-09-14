import sys

import mymodule
print("Import.py", __name__)
print(mymodule.divide(10, 2))

# Same as:
# If we don't want to import a specific stuff, like divide, then use "import mymodule"
#from mymodule import divide

#print("Import.py", __name__)
#print(divide(10, 2))

# How does python knows where is my mymodule is? And: 'sys' where Pythin will look to find file to import
# Sequence: 1st Loc is the location where the file present, second is classpath and so on...
print(sys.path)
print(sys.modules)
