def factorial(n):
    if n < 1:
        return 1
    else:
        return n * factorial(n-1)

number = str(factorial(100))
result = 0
for num in number:
    result += int(num)

print(f"Sum of digits 100! is {result}")