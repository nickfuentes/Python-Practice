class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age


class Grandfather(Person):
    def __init__(self, name, age):
        super().__init__(name, age)
        self.occupation = ""

    def walk(self):
        print("Walk slow!")


class Father(Grandfather):
    def __init__(self, name, age):
        super().__init__(name, age)
        self.hobby = ""
        self.job = ""

    def walk(self):
        print("Walk fast")


class Kid(Father):
    def __init__(self, name, age=""):  # kid = Kid("Jerry")
        super().__init__(name, age)
        #self.age = ""
        self.toys = ["Airplane", "Car"]


kid = Kid("Jerry", 26)
print(kid.name)
print(kid.age)
print(kid.hobby)
