def largest_prime_factor(n):
    i = 2
    while i * i <= n:
        if n % i == 0:
            n //= i
        else:
            i += 1
    return n

number = 600851475143
result = largest_prime_factor(number)
print(result)