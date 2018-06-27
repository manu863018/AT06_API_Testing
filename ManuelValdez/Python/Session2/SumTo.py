def sum_to(n):
    sum = 0
    for i in range(1, n + 1):
        sum += i
        if (i > 34):
            return sum
    return sum

print(sum_to(10))
print(sum_to(40))
print(sum_to(20))
print(sum_to(30))
print(sum_to(35))