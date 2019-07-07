import json


class Customer:
    def __int__(self, name, age):
        self.name = name
        self.age = age

    @staticmethod
    def from_dictionary(dict):
        return Customer(dict["Name"], dict["Age"])

    def to_dictionary(self):
        return {
            "name": self.name
            "age": self.age
        }


customer = Customer("John", 34)
print(customer.__dict__)  # customer.__dict__


with open("customers.json", "w") as file_object:
    json.dump(customer.__dict__, file_object)
