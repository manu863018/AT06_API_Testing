def tableOfLetters(text):
    table = {}
    text = text.replace(" ", "")
    for letter in text.lower():
        if letter in table:
            table[letter.lower()] = table[letter.lower()] + 1
        else:
            table[letter.lower()] = 1
    return orderDictionary(table)


def orderDictionary(dictionary):
    orderedTable = {}
    for orderedKey in sorted(dictionary.keys()):
        orderedTable[orderedKey] = dictionary[orderedKey]
    return orderedTable


def printDictionary(dictionary):
    for key in dictionary:
        print(key, " ", dictionary[key])


printDictionary(tableOfLetters("ThiS is String with Upper and lower case Letters"))
print("\n")
printDictionary(tableOfLetters("a"))
print("\n")
printDictionary(tableOfLetters(""))
print("\n")
printDictionary(tableOfLetters("COUNT"))
print("\n")
printDictionary(tableOfLetters(" "))
print("\n")