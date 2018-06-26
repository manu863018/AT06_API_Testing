def perform_operation(operationSign, firstArgument, secondArgument):
    firstArgument = int(firstArgument)
    secondArgument = int(secondArgument)
    if (operationSign == "+"):
        return firstArgument + secondArgument
    elif (operationSign == "-"):
        return firstArgument - secondArgument
    elif (operationSign == "*"):
        return firstArgument * secondArgument
    elif (operationSign == "/"):
        return firstArgument / secondArgument
    elif (operationSign == "%"):
        return firstArgument % secondArgument
    elif (operationSign == "**"):
        return firstArgument ** secondArgument
    elif (operationSign == "//"):
        return firstArgument // secondArgument
    else:
        return "No defined operation sign"

print("result1:", perform_operation("+", "10", "3"))
print("result2:", perform_operation("-", "10", "3"))
print("result3:", perform_operation("*", "10", "3"))
print("result4:", perform_operation("/", "10", "3"))
print("result5:", perform_operation("%", "10", "3"))
print("result6:", perform_operation("**", "10", "3"))
print("result6:", perform_operation("//", "10", "3"))
print("result6:", perform_operation("&", "10", "3"))
