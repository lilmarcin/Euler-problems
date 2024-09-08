def divisors(n):
    total = 0
    for i in range(1, n):
        if n % i == 0:
            total += i
    return total

amicable_number = 0
for num in range (1,10000):
    first_res = divisors(num)
    second_res = divisors(first_res)
    if second_res == num and num != first_res:
        #print(f"d{num} == {first_res}, d{first_res} == {second_res}")
        amicable_number += num
print(amicable_number)

