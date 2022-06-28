name = "Sushanta"
print(f"Hello {name}")
name = "Tutun"
print(f"Hello {name}")

print("Another way with template")
name1 = "Sushanta"
greeting = "Hello {}"
with_name = greeting.format(name1)
with_name2 = greeting.format("Tutun")
print(with_name)
print(with_name2)


another = "Hello {} and {}".format("zzzzzzzzzzzzzzzzzz", "xxxxxxxxxx")
print(another)
