firstVariable = 6
secondVariable = -1
numbersArray = [-6, -5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5, 6]

if (firstVariable in numbersArray):
    print(firstVariable, "exists in ", numbersArray)

if (10 in numbersArray):
    print(10, "exists in ", numbersArray)
else:
    print(10, "does not exist in ", numbersArray)

if (secondVariable not in numbersArray):
    print(secondVariable, "does not exist in ", numbersArray)
else:
    print(secondVariable, "exists in ", numbersArray)

if (30 not in numbersArray):
    print(30, "does not exist in ", numbersArray)