def sum_of_the_squares(n):
    result = 0
    for i in range(1, n+1):
        result += i**2
    return result

def square_of_the_sum(n):
    result = 0
    for i in range(1, n+1):
        result += i
    return result**2

square_sum  = sum_of_the_squares(100)
sum_squares = square_of_the_sum(100)
difference = sum_squares - square_sum
print(difference)