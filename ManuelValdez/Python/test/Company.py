from utils.Utils import getUserId


class Company:

    def __init__(self):
        self.employees = {}


    def fillEmployees(self, employee):
        self.employees[getUserId(employee.getType(), self.employees)] = employee


    def printEmployeesReport(self):
        print("Employee ID | Name | Department | Global Salary | Total Discount | Net Salary")
        for emp in self.employees:
            print("{}|{}|{}|{}|{}|{}".format(emp, self.employees[emp].getName(), self.employees[emp].getType(),
                  self.employees[emp].calculateGlobalSalary(),
                  self.employees[emp].calculateDiscount(self.employees[emp].calculateGlobalSalary()),
                  self.employees[emp].calculateNetSalary(self.employees[emp].calculateGlobalSalary(), self.employees[emp].calculateDiscount(self.employees[emp].calculateGlobalSalary()))))
