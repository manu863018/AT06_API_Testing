def push_array():
    numberOfElements = int(input("Insert number of elements: "))
    arrayOfElements = []
    for element in range(numberOfElements):
        newElement = input("insert element in position " + str(element) + ": ")
        arrayOfElements.append(newElement)
    return(arrayOfElements)


def print_array(array):
    print("array:", array)


array = push_array();
print_array(array)

