def fibonacci(a, b, limit, sum_even):
    if a > limit:
        return sum_even
    if a % 2 == 0:
        sum_even += a
    return fibonacci(b, a + b, limit, sum_even)

limit = 4000000
result = fibonacci(1, 2, limit, 0)
print(result)