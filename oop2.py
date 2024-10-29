class Person:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    def show(self):
        print(f"{self.name} is {self.age} years old. He is {self.gender}")

my_person = Person("Nathan", 24 ,"Male")
my_person.show()