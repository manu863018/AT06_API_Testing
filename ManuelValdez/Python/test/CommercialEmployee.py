from Employee import Employee


class CommercialEmployee(Employee):

    def __init__(self, type, amount, name):
        super().__init__(type, name)
        self.amountOfPiecesSold = amount


    def calculateGlobalSalary(self):
        return self.amountOfPiecesSold * 2.5


