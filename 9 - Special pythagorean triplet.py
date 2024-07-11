def pythagorean_triplet(sum_of_abc):
    for a in range(1, sum_of_abc):
        for b in range(a + 1, sum_of_abc):
            c = sum_of_abc - a - b
            if c > b:
                if a*a + b*b == c*c:
                    return a, b, c
    return 0

sum_of_abc = 1000
triplet = pythagorean_triplet(sum_of_abc)

a, b, c = triplet
product = a * b * c
print(a,b,c)
print(product)

