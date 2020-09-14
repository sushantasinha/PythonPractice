def divide(numerator, denominator):
    if denominator == 0:
        raise ZeroDivisionError("Denominator can not be zero")
    return numerator / denominator


def calculate(*values, operator):
    return operator(*values)


result = calculate(20, 4, operator=divide)
print(result)

# Learn below:
# from operator import itemgetter
