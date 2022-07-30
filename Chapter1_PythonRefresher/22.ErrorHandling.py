def divide(numerator, denominator):
    if denominator == 0:
        raise ZeroDivisionError("Denominator can not be zero") #...
    return numerator / denominator


try:#...
    average = divide(10, 0)
    print(f"Result: {average}")
except ZeroDivisionError as e:#...
    print(e)
    print("Error occurred: ZeroDivisionError.")


try:
    average = divide(10, 0)
except ZeroDivisionError as e:
    print(e)
    print("Error occurred: ZeroDivisionError.")
except ValueError:
    print("Error occurred: ValueError.")
else:  # if no error happened then use this section #...
    print(f"Result: {average}")
finally:#...
    print("In Finally")
