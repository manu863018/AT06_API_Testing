from Ages import calculateAgeInDays, calculateAgeInHours, calculateAgeInMinutes
from AgesMessages import agesMessages

users = {}
amountOfUsers = int(input("insert the amount of users: "))
for user in range(amountOfUsers):
    name = input("insert user's name: ")
    age = int(input("insert user's age: "))
    users[name] = age
for key in users:
    print(key, ", age:", users[key], ", in minutes:", calculateAgeInMinutes(users[key]), ", in hours:", calculateAgeInHours(users[key]), ", in days:", calculateAgeInDays(users[key]))
    agesMessages(users[key])


