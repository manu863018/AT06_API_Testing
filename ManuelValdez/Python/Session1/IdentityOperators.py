firstVariable = 10
secondVariable = 10

if (firstVariable is secondVariable):
    print(firstVariable, "points to the same object than", secondVariable)

thirdVariable = 20

if (firstVariable is thirdVariable):
    print(firstVariable, "points to the same object than", thirdVariable)
if (firstVariable is not thirdVariable):
    print(firstVariable, "does not point to the same object than", thirdVariable)

print(firstVariable, "identity is:", id(firstVariable))
print(secondVariable, "identity is:", id(secondVariable))
print(thirdVariable, "identity is:", id(thirdVariable))