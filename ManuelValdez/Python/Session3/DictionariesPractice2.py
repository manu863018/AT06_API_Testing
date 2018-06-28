def dictionaryBetween1And9():
    """function to fill a dictionary with keys only numbers, max limit 1, min limit 9"""
    dictionary = {}
    while (True):
        key = int(input("insert key: "))
        if (key < 1 or key > 9):
            break
        dictionary[key] = key ** 2
    return dictionary


def printPrimeDictionary(dictionary):
    """function to print only prime keys from a dictionary"""
    primeDictionary = {}
    for key in dictionary.keys():
        for div in range(2, key - 1):
            if (key % div == 0):
                break
        else:
            primeDictionary[key] = dictionary[key]
    print(primeDictionary)

printPrimeDictionary(dictionaryBetween1And9())
