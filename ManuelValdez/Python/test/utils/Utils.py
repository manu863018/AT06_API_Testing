from re import match


def getUserId(code, employees):
    if len(employees) == 0:
        return "{}_001".format(code)
    coincidences = getArrayOfCoincidences(code, employees)
    return "{}_00{}".format(code, len(coincidences) + 1)

def getArrayOfCoincidences(code, employees):
    arrayOfCoincidences = []
    for index in employees:
        regex = "^{}".format(code)
        if match(regex, index):
            print(index)
            arrayOfCoincidences.append(index)
    return arrayOfCoincidences
