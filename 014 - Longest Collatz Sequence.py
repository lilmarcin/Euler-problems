def collatz_sequence_length(n):
    length = 1
    while n != 1:
        if n % 2 == 0:
            n //= 2
        else:
            n = 3 * n + 1
        length += 1
    return length

def longest_collatz(n):
    chain_length = {}
    max_counter = 0
    number_with_max_chain = 0
    for i in range(1, n):
        if i % 10000 == 0:
            print(f"checking number {i}")
        length = collatz_sequence_length(i)
        chain_length[i] = length
        if length > max_counter:
            max_counter = length
            number_with_max_chain = i
    print(f"max chain length: {max_counter} for number {number_with_max_chain}")
    return max_counter

number = 1000000
result = longest_collatz(number)
print(result)
