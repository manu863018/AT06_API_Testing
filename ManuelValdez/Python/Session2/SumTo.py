def sum_to(n):
    sum = 0
    for i in range(1, n + 1):
        print ("i:",i)
        sum += i
        if (i > 33):
            return sum
    return sum

print(sum_to(10))
print(sum_to(40))