# Dictionaries
units = {
    1: 'one', 2: 'two', 3: 'three', 4: 'four', 5: 'five',
    6: 'six', 7: 'seven', 8: 'eight', 9: 'nine'
}

teens = {
    10: 'ten', 11: 'eleven', 12: 'twelve', 13: 'thirteen',
    14: 'fourteen', 15: 'fifteen', 16: 'sixteen',
    17: 'seventeen', 18: 'eighteen', 19: 'nineteen'
}

tens = {
    20: 'twenty', 30: 'thirty', 40: 'forty', 50: 'fifty',
    60: 'sixty', 70: 'seventy', 80: 'eighty', 90: 'ninety'
}

hundred = 'hundred'
thousand = 'thousand'

def number_to_words(n):
    if n == 1000:
        return 'one thousand'
    words = ''
    if n >= 100:
        words += units[n // 100] + ' hundred'
        if n % 100 != 0:
            words += ' and '
        n %= 100
    if n >= 20:
        words += tens[n // 10 * 10]
        if n % 10 != 0:
            words += '-' + units[n % 10]
    elif n >= 10:
        words += teens[n]
    elif n > 0:
        words += units[n]
    return words




def count_letters(word):
    return len(word.replace(' ', '').replace('-', ''))

total_letters = 0
for i in range(1, 1001):
    words = number_to_words(i)
    total_letters += count_letters(words)
print(f"To write numbers from 1 to 1000, we need to use {total_letters} letters")

