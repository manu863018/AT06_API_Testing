def primeOrNot(min, max):
    list = range(min, max + 1)
    for i in list:
        for div in range(2, i - 1):
            if (i % div == 0):
                print(i, "is not prime")
                break
        else:
            print(i, "is prime")



primeOrNot(1, 11)