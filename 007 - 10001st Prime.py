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

def finding(n):
    counter = 0
    number = 1
    while counter < n:
        number += 1
        if is_prime(number):
            #print(number)
            counter += 1
    return number

n = 10001
result = finding(n)
print(result)