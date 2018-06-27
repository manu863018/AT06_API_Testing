def days_in_month(month):
    year = {"January": 31 ,
            "February": 28,
            "March": 31,
            "April": 30,
            "May": 31,
            "June": 30,
            "July": 31,
            "August": 31,
            "September": 30,
            "October": 31,
            "November": 30,
            "December": 31}
    if (month not in year): return None
    return year[month]

print("January has", days_in_month("January"), "days")
print("February has", days_in_month("February"), "days")
print("March has", days_in_month("March"), "days")
print("April has", days_in_month("April"), "days")
print("May has", days_in_month("May"), "days")
print("June has", days_in_month("June"), "days")
print("July has", days_in_month("July"), "days")
print("August has", days_in_month("August"), "days")
print("September has", days_in_month("September"), "days")
print("October has", days_in_month("October"), "days")
print("November has", days_in_month("November"), "days")
print("December has", days_in_month("December"), "days")
print("Month has", days_in_month("Month"), "days")

