class Student:
    name1 = "zzz"

    def __init__(self, name):  # like constructor
        # self.name = "Sushanta"  # The self is used to represent the instance of the class.
        self.name = name
        self.grades = (10, 20, 30)
        self.name2 = "xxx"

    def avg(self):  # Every method inside class has to take a param which will be the obj that was created initially
        return sum(self.grades) / len(self.grades)


student = Student("Hello...")
print(student.name)
print(student.name1)
print(student.avg())  # student obj will be passed implecitly
print(student.name2)
print(student)


# Any method name __<method name>__(): is magic called method, these are provided by python


class Person:

    def __init__(self, name, age):  # like constructor
        self.name = name
        self.age = age

    def __str__(self):  # like toString()
        return f"Name is {self.name} and age is {self.age}"

    def __repr__(
            self):  # wrapper method. __repr__ is for developers, __str__ is for customers. __repr__ goal is to be unambiguous. __str__ goal is to be readable.
        return f"<Person {self.name}, {self.age}>"

    # Now if you go by the official python documentation – the __str__ is used to find the “informal”(readable) string representation
    # of an object whereas __repr__ is used to find the “official” string representation of an object.


person = Person("Bob", 25)
print(person)  # if we want to see reponse of __repr__, then commented out __str__


# We can __str__, __init__ etc manually as well like, persom.___init()


class ClassTest:
    def instance_method(self):  # self if the reference of the obj
        print(f"Called instance_method of {self}")

    @classmethod
    def class_method(cls):  # cls is reference of ClassTest. used mostly for Factory.
        print(f"Called class_method of {cls}")

    @staticmethod
    def static_method():  # don't get cls or self i.e. does not have cls reference or instance reference
        print("Called static_method")


test = ClassTest()
test.instance_method()  # same as ClassTest.instance_method(test)
ClassTest.instance_method(test)
ClassTest.class_method()
ClassTest.static_method()


class Book:
    TYPES = ("hardcover", "paperback")

    def __init__(self, name: str, book_type: str, weight: int):
        self.name = name
        self.book_type = book_type
        self.weight = weight

    def __repr__(self) -> str:
        return f"<Book {self.name}, {self.book_type}, weight {self.weight}g>"

    @classmethod
    def hardcover(cls, name: str, page_weight: str) -> "Book":
        return cls(name, Book.TYPES[0], page_weight + 100)

    @classmethod
    # Please see the return type a "Book" instead of Book (without code).
    # This is needed as Book class definition is NOT completed yet and we are using it
    # I.e. we are taking Book ref from within Book class
    # If return type say BookShelf then douple quite is not needed
    def paperback(cls, name: str, page_weight: str) -> "Book":
        return cls(name, cls.TYPES[1], page_weight)

    # Same as below
    # @classmethod
    # def paperback(cls, name, page_weight):
    #     return Book(name, Book.TYPES[1], page_weight)

    # We can use static method as well but here we need to use Book and NOT cls
    # '@staticmethod
    # def paperback(name, page_weight):
    #    return Book(name, Book.TYPES[1], page_weight)


book = Book.hardcover("Harry Potter", 1500)
print(book)

book = Book.paperback("Harry Potter", 1500)
print(book)
