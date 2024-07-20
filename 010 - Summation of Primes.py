def is_prime(n):
    if n <=1:
        return False
    if n <=3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i*i <=n:
        if n % i == 0 or n % (i+2) == 0:
            return False
        i += 6
    return True

def summation(n):
    result = 0
    number = 1
    while number < n:
        number += 1
        if is_prime(number):
            result += number
    return result

n = 2000000
result = summation(n)
print(result)
