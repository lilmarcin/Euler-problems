def is_palindrome(n):
    return str(n) == str(n)[::-1]

def largest_palindrome_product():
    max_palindrome = 0
    
    for i in range(999, 100, -1):
        for j in range(i, 100, -1):
            product = i * j
            if is_palindrome(product) and product > max_palindrome:
                max_palindrome = product
                
    return max_palindrome

result = largest_palindrome_product()
print(result)
