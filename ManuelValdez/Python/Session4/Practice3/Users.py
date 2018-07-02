# Function to display a message considering :
    # UseID between 1-25 “User belong Group 1”
    # UseID between 26-50 “User belong Group 2”
    # UseID between 51-75 “User belong Group 3”
    # UseID between 76-100 “User belong Group 4”

from re import fullmatch


users = {}
def createUsersDictionary():
    global users
    while int(input("insert new user? 0 to exit, 1 to continue: ")):
        userId = int(input("insert user id: "))
        if (userId < 1 or userId > 100):
            print("user id must be between 1 and 100")
            continue
        userName = input("insert user name: ")
        if not fullmatch("^[a-z]{0,8}", userName):
            print("user name must be only lowercase no more than 8 digits")
            continue
        users[userId] = userName
    print(users)


def usersWithIdStartingIn():
    numberToSearch = int(input("insert number to search in users id: "))
    fulfilledNumber = []
    regex = "^{}".format(numberToSearch)
    for user in users:
        if fullmatch(regex, str(user)):
            fulfilledNumber.append(user)
    print("number of users:", len(fulfilledNumber))
    return fulfilledNumber


def usersWithNameStartingIn():
    characterToSearch = input("insert character to search in users name: ")
    fulfilledCharacter = []
    regex = "^{}".format(characterToSearch)
    for user in users:
        if fullmatch(regex, users[user]):
            fulfilledCharacter.append(users[user])
    print("number of users:", len(fulfilledCharacter))
    return fulfilledCharacter

def displayUserGroup():
    for user in users:
        if user > 0 and user < 26:
            print("User belong Group 1")
        elif user > 25 and user < 51:
            print("User belong Group 2")
        elif user > 50 and user < 76:
            print("User belong Group 3")
        elif user > 75 and user < 101:
            print("User belong Group 4")
        else:
            print("User does not belong to any group")


createUsersDictionary()
print(usersWithIdStartingIn())
print(usersWithNameStartingIn())
displayUserGroup()