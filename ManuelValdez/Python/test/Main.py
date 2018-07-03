from Company import Company
from CommercialEmployee import CommercialEmployee
from ProductionEmployee import ProductionEmployee
from utils.Log import Log


log = Log()
logger = log.getLoggerInstance()

logger.info("Start Main Script")
logger.debug("Instance of Company Class")
company = Company()
logger.info("Amount of employees")
amountOfEmployees = int(input("How many employees would you register? "))
logger.debug("Amount of employees %s", amountOfEmployees)
try:
    if (amountOfEmployees < 4 or amountOfEmployees > 16):
        myError = ValueError("The amount of employees should be no less than 3 and no more than 15")
        logger.info(myError)
        raise myError
except ValueError:
    logger.debug("amount of employees %s", amountOfEmployees)
    print(myError)
else:
    logger.info("amount correct, start process")
    for amount in range(1, amountOfEmployees + 1):
        logger.debug("Employee %s", amount)
        employeeName = input("Employee number {}, insert name: ".format(amount))
        logger.debug("name %s", employeeName)
        typeOfEmployee = input("Employee number {}, insert type: ".format(amount))
        logger.debug("type %s", typeOfEmployee)
        if typeOfEmployee == "CE":
            logger.info("new Commercial employee")
            amountOfPiecesSold = int(input("Amount of pieces sold: "))
            logger.debug("pieces sold %s", amountOfPiecesSold)
            employee = CommercialEmployee(typeOfEmployee, amountOfPiecesSold, employeeName)
        else:
            logger.info("new production employee")
            amountOfPiecesProduced = int(input("Amount of pieces produced: "))
            logger.debug("pieces produced %s", amountOfPiecesProduced)
            amountOfPiecesDefective = int(input("Amount of pieces defective found: "))
            logger.debug("pieces defective %s", amountOfPiecesDefective)
            employee = ProductionEmployee(typeOfEmployee, amountOfPiecesProduced, amountOfPiecesDefective, employeeName)
        logger.info("fill company employees")
        company.fillEmployees(employee)
    logger.info("print company employees")
    company.printEmployeesReport()