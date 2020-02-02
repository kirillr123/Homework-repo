import string


def letters_range(first_letter = 'a', last_letter = 'z', step=1):
    alphabet = list(string.ascii_lowercase)
    return alphabet[alphabet.index(first_letter):alphabet.index(last_letter):step]


print(letters_range('b', 'w', 2))
print(letters_range('a', 'g'))
print(letters_range('g', 'p'))
print(letters_range('p', 'g', -2))
print(letters_range('a', 'a'))
