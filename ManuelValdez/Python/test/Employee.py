from Person import Person


class Employee(Person):
    def __init__(self, type, name):
        super().__init__(name)
        self.type = type
        global discount

    def getType(self):
        return self.type


    def calculateDiscount(self, globalSalary):
        return (12.5 / 100) * globalSalary


    def calculateNetSalary(self, globalSalary, discount):
        return globalSalary - discount