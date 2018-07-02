from Person import Person


class Employee(Person):

    def __init__(self, emp_id, dep, name, lastName, age, ci):
        super().__init__(name, lastName, age, ci)
        self.employee_Id = emp_id
        self.department = dep


    def printAttributes(self):
        super().printAttributes()
        print("Employee Id:", self.employee_Id, ",Department:", self.department)