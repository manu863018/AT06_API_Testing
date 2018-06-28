dictionary = {}
def createDictionary():
    """function to create a dictionary with user length, keys and values"""
    dictionaryLength = int(input("insert the length of the dictionary: "))
    global dictionary
    for i in range(dictionaryLength):
        key = input("insert key: ")
        value = input("insert value: ")
        if (not isKeyInDictionary(key) and not isValueInDictionary(value)):
            dictionary[key] = value


def printDictionaryKeys():
    """function to print dictionary keys"""
    print("Keys")
    for key in dictionary.keys():
        print(key)


def printDictionaryValues():
    """function to print dictionary values"""
    print("Values")
    for value in dictionary.values():
        print(value)


def printDictionary():
    """function to print dictionary"""
    print("Key Value")
    for key in dictionary:
        print(key, "", dictionary[key])


def isKeyInDictionary(key):
    if (key in dictionary.keys()):
        print("key:", key, ",exists in dictionary", dictionary)
        return True
    else:
        return False


def isValueInDictionary(value):
    if (value in dictionary.values()):
        print("value:", value, ",exists in dictionary", dictionary)
        return True
    else:
        return False



newDictionary = createDictionary()
printDictionaryKeys()
printDictionaryValues()
printDictionary()