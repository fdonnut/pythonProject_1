en_lower = 'abcdefghijklmnopqrstuvwxyz'
en_upper = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'


def encoded(k, t):
    phrase = ''
    for i in range(len(t)):
        if t[i] in en_upper:
            phrase += en_upper[(en_upper.index(t[i]) + k) % len(en_upper)]
        elif t[i] in en_lower:
            phrase += en_lower[(en_lower.index(t[i]) + k) % len(en_lower)]
        else:
            phrase += t[i]
    return phrase


text = 'Day, mice. "Year" is a mistake!'
text = text.split()
phrase = ''
for i in range(len(text)):
    count = 0
    for j in range(len(text[i])):
        if text[i][j].isalpha():
            count += 1
    print(encoded(count, text[i]), end=' ')
