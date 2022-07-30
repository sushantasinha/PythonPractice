#...

# List: Can modify. Guarantee the order of the list.
l = ["Name1", "Name2", "Name2"]
print(l)

# Tuple: Same as list. But this is immutable i.e. we can't modify a tuples. Guarantee the order of the list.
# Kind of concept of Java ENUM
t = ("Name1", "Name2", "Name2")
print(t)

# Set: Can not insert duplicate. Can not guarantee the order of the list.
s = {"Name1", "Name2", "Name2"}
print(s)

# Access List or Tuple elements:
print(l[0])
print(t[0])

# print(s[1]): Won't work

l[0] = "Updated Name"
print(l)

# t[0] = "Updated Name": Won't work

l.append("Name3")
print(l)

l.remove("Name2")  # this will remove only 1 element, as we have 2 Name2 in the list, will delete only the first one
print(l)

# We can not add or remove elements from Tuple

s.add("Name20")
s.add("Name20")
s.remove("Name1")
print(s)

# Advanced sets operations

print("Advanced sets operations::::::::::::::::::::::")
all_friends = {"friend1", "friend2", "friend3"}
abroad_friends = {"friend1", "friend3"}

print(abroad_friends.difference(all_friends))
print(all_friends.difference(abroad_friends))

print(":::::::::::::::::::::::")
local_friends = all_friends.difference(abroad_friends)
print(local_friends)
print(abroad_friends.difference(all_friends))

# Create empty set: set()
print(abroad_friends.union(local_friends))

# Set Intersection
art = {"name1", "name2", "name3"}
science = {"name1", "name3", "name4"}
both = art.intersection(science)
print(both)

my_list = [70, 20, 10]

# Create a tuple with single element
my_tuple = (15,) # or just 15, \If single element, then need to append comma
print(my_tuple[0])

# x = (1,2) and x = 1,2 => both are tuple -> but bracket is needed if we use tuple inside list -> x = [(1,2)]