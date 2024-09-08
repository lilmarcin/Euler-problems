def Divisors(n):
    result = 0
    for i in range(1, n):
        if n % i == 0:
            print(f"Dodaje {i}")
            result += i
    return result


# generate abundant
abundant = []
for i in range(12, 28123):
    proper_divisors = Divisors(i)
    if proper_divisors > i:
        abundant.append(i)
print(abundant)