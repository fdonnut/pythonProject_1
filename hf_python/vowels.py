from pprint import pprint

vowels = ['a', 'e', 'i', 'o', 'u']
word = input("your word: ")

found = {}

for letter in word:
    if letter in vowels:
        found.setdefault(letter, 0)
        found[letter] += 1

for k, v in sorted(found.items()):
    print(k, 'was found', v, 'time(s).')

# for letter in word:
#     if letter in vowels:
#         if letter not in found:
#             found.append(letter)
# for vowel in found:
#     print(vowel)

vo = set('aeiou')
wo = 'hello'
u = vo.union(set(wo))
u_list = sorted(list(u))
print(u_list)
d = vo.difference(set(wo))
print(d)

people = {}
people['Ford'] = {'Name': 'Ford Prefect',
                  'Gender': 'Male',
                  'Occupation': 'Researcher',
                  'Home Planet': 'Betelgeuse Seven'}
people['Arthur'] = {'Name': 'Arthur Dent',
                    'Gender': 'Male',
                    'Occupation': 'Sandwich-Maker',
                    'Home Planet': 'Earth'}
people['Trillian'] = {'Name': 'Tricia McMillan',
                      'Gender': 'Female',
                      'Occupation': 'Mathematician',
                      'Home Planet': 'Earth'}
people['Robot'] = {'Name': 'Marvin',
                   'Gender': 'Unknown',
                   'Occupation': 'Paranoid Android',
                   'Home Planet': 'Unknown'}
pprint(people)


def search4v():
    vol = set('aeiou')
    w = input("your word: ")
    f = vol.intersection(set(w))
    for o in f:
        print(o)
