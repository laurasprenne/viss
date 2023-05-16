# abstrakcija - neļauj piekļūt lietotājam nevajadzīgām funkcijām
# mantošana - manto funkcijas no vecākas klases
# polimorfisms - 

class Person:
    def __init__(self, vards, uzvards, pk):
        self.vards = vards
        self.uzvards = uzvards
        self.pk = pk

    def fullName(self):
        return self.vards + " " + self.uzvards

class Teacher(Person):
    def priekšmets(self, priekšmets):
        self.priekšmets = priekšmets

    def dati(self):
        print(self.fullName(), self.priekšmets)

class Student(Person):
    def klase(self, klase):
        self.klase = klase

    def setIntereses(self):
        self.intereses = []
        interese = input("ievadi interesi: ")
        while len(interese) > 0:
            self.intereses.append(interese)
            interese = input("ievadi interesi: ")
            
    def getIntereses(self):
        if self.intereses:
            for interese in self.intereses:
                print(interese)
        

skolotajs = Teacher("Atis", "Ozols", "1234-5678")
skolotajs.priekšmets("programmēšana")
skolotajs.dati()
students = Student("Laura", "Sprenne", "8765-4321")
students.setIntereses()
students.getIntereses()