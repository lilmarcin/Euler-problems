def number_divisors(n):
    factors = []
    for i in range(1, n+1):
        if n % i == 0:
            factors.append(i)
    return factors


def triangle_numbers(target):
    n = 1
    sequence = 0
    while True:
        sequence += n
        factors = number_divisors(sequence)
        #print(f"number {sequence} has {len(factors)} factors: {factors}")
        if len(factors) > 100:
            print(f"number {sequence}, factors > 100")
        if len(factors) > 200:
            print(f"number {sequence}, factors > 200")
        if len(factors) > 300:
            print(f"number {sequence}, factors > 300")
        if len(factors) > 400:
            print(f"number {sequence}, factors > 400")
        if len(factors) > 500:
            print(f"number {sequence}, factors > 500")
        if len(factors) > target:
            return sequence
        n += 1
        

number = 200
result = triangle_numbers(number)
print(result)


