with open('names.txt', 'r') as file:
    lines = file.readlines()
names = [name.strip().strip('"') for name in lines[0].split(',')]

alphabet = {
    'A' : 1,
    'B' : 2,
    'C' : 3,
    'D' : 4,
    'E' : 5,
    'F' : 6,
    'G' : 7,
    'H' : 8,
    'I' : 9,
    'J' : 10,
    'K' : 11,
    'L' : 12,
    'M' : 13,
    'N' : 14,
    'O' : 15,
    'P' : 16,
    'Q' : 17,
    'R' : 18,
    'S' : 19,
    'T' : 20,
    'U' : 21,
    'V' : 22, 
    'W' : 23,
    'X' : 24,
    'Y' : 25,
    'Z' : 26,
}

total = 0
for index, name in enumerate(names):
    cost = sum(alphabet[char] for char in name)
    print(f"index: {index}, name: {name}, cost: {cost}")
    total += index * cost
print(total)