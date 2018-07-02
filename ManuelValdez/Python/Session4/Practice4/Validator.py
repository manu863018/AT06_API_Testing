from re import fullmatch

def validateUsername():
    userName = input("insert username: ")
    if not fullmatch("^[a-z0-9_]*$", userName):
        print("username:", userName, ", must be written with lowecase (a-z), number (0-9), underscore")


def validatePassword():
    password = input("insert password: ")
    if not fullmatch("^[a-zA-Z0-9]{8,16}$", password):
        print("password:", password, ", must be written with lowecase (a-z), number (0-9), letter (A-1) and be between 8 and 16 characters long")


def validateEmail():
    email = input("insert email: ")
    if not fullmatch("(^\w*\@\w*\.\w{3}\.\w{2}$|^\w*\@\w*\.\w{3}$)", email):
        print("email:", email, "should have the format anything@domain.com or anything@domain.com.bo")


validateUsername()
validatePassword()
validateEmail()