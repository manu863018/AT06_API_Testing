from Employee import Employee


class ProductionEmployee(Employee):
    def __init__(self, type, amountProd, amountDef, name):
        super().__init__(type, name)
        self.amountOfPiecesProduced = amountProd
        self.amountOfPiecesDefective = amountDef

    def calculateGlobalSalary(self):
        return self.amountOfPiecesProduced * 10 +  self.amountOfPiecesDefective * 1.3




