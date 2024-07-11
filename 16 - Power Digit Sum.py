import math

def power_digit_sum(n):
    power = int(math.pow(2,n))
    digits = str(power)
    # total = 0
    # for num in digits:
    #     total += int(num)
    # return total
    return sum(int(digit) for digit in digits)


num = 1000
result = power_digit_sum(num)
print(result)