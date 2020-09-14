# from lib.operations import operator
# Relative import. Below is also work
from .operations import operator

# Recommended to use absolute import as much as possible

# Please note, if we by any reason run mylib.py directly to debug or so it will NOT work with relative import.
# As, it will be main class and there is NO folder hierarchy

print("mylib.py", __name__)
