class Person:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname

    def fullName(self):
        return self.name + " " + self.surname

class Student(Person):
    aplNr = "ls12345"

laura = Student("Laura", "Sprenne")
print(laura.fullName())

