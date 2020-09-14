name = input("Enter your name:")
print(f"Hello {name}")

size_input = input("How big is your house (in feet): ")
size_feet = float(size_input)
size_meter = size_feet / 10.8
print(f"{size_feet} square feet is {size_meter} square meters.")
print(f"{size_feet} square feet is {size_meter:.2f} square meters.")

# We can use below as well
# size_input = int(input("How big is your house (in feet): "))
