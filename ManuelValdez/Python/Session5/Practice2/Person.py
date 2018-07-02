class Person:

    def __init__(self, name, lastName, age, ci):
        self.name = name
        self.lastName = lastName
        self.age = age
        self.ci = ci


    def printAttributes(self):
        print("Name:", self.name, ",Last Name:", self.lastName, ",Age:", self.age, ",CI:", self.ci)