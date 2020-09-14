def add_old(x, y):
    return x + y


print(add_old(1, 2))

add_new = lambda x, y: x + y
print(add_new(1, 2))
print((lambda x, y: x + y)(1, 2))


def double(x):
    return x * 2


sequence = [1, 2, 3, 4]
doubled_sequence = [x * 2 for x in sequence]
print(doubled_sequence)
doubled_sequence = [double(x) for x in sequence]
print(doubled_sequence)
doubled_sequence = list(map(double, sequence))
print(list(doubled_sequence))
doubled_sequence = list(map(lambda x: x*2, sequence))
print(list(doubled_sequence))
