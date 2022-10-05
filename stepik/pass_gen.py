import random

digits = '0123456789'
lowercase_letters = 'abcdefghijklmnopqrstuvwxyz'
uppercase_letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
punctuation = '!#$%&*+-=?@^_'
exceptions = 'iIl1Lo0O'

chars = [digits, lowercase_letters, uppercase_letters, punctuation, exceptions]
length = random.randint(8, 12)


def generate(length, chars):
    password = ''
    while len(password) <= length:
        num_lst = random.randint(0, len(chars) - 2)
        c = random.choice(chars[num_lst])
        if c not in chars[-1]:
            password += c
        continue
    print(password)
    return password


generate(length, chars)

