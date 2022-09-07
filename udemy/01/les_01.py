greeting = 'hello python'
print(len(greeting))
greeting_length = len(greeting)
print(greeting, greeting_length)
x = 7
print(x + greeting_length)
print(greeting[3])
print(greeting[-1])
print(greeting[2:-1:3])
print(greeting[2::3])
print(greeting[2::2])
print(greeting[::-1])
name = 'jake'
name = name[:2] + 'n' + name[-1]
print(name)
print(name.upper())
name = name[0].upper() + name[1:]
print(name)
name = name.lower()
print(name)
print(1 + 1)
print('1' + '1')
age = 23
print(name + ' is ' + str(age) + ' years old.')
name_and_age = 'my name is {0}. i\'m {1} years old.'.format(name, age)
print(name_and_age)
week_days = '7 дней недели: {}, {}, {}, {}, {}, {}, {}'.format('пн', 'вт',
                                                               'ср', 'чт',
                                                               'пт', 'сб', 'вс')
print(week_days)
fl_res = 1000 / 7
print(fl_res)
print('result is {0:1.2f}'.format(fl_res))

name_and_age = f'my name is {name}. i\'m {age} years old.'
print(name_and_age)
# lists
number_list = [32, 12, 23, 4.7]
print(number_list)
some_list = [12, 67, 89, 45, 34]
print(some_list)
print(len(number_list), len(some_list))
print(some_list[2:4])
number_list[3] = 56
print(number_list)
new_list = number_list + some_list
new_list.sort()
new_list.reverse()
new_list.pop()
print(new_list)
another_list = ['hi', 23, 45, 56, 78, 'hello']
deleted_item = [another_list.pop(), another_list.pop(0)]
print(another_list)
print(deleted_item)
# dict
car_prices = {'opel': 1200, 'toyota': 3000, 'bmw': 5000}
print(car_prices)
print(car_prices['bmw'])
car_prices['mazda'] = 2500
del car_prices['toyota']
print(car_prices)
# car_prices.clear()

person = {'first name': 'jack',
          'last name': 'brown',
          'age': 43,
          'hobbies': ['football', 'singing', 'photo'],
          'children': {'son': 'michael',
                       'daughter': 'pamela'}}

print(person['age'])
print(person['hobbies'][1])
print(person['children']['son'])
person['car'] = 'mazda'
print(person)
print(person.keys())
print(person.values())
print(person.items())
# tuple
tuple_1 = (1, 2, 3)
tuple_2 = ('one', 'two', 'three')
print(tuple_1)
print(tuple_2[1])
x, y, z = 12, 13, 14
print(id(x), id(y), id(z))
x, y, z = tuple_2
print(x, y, z)
# set
rainbow_colors = {'red', 'orange', 'yellow', 'green', 'blue', 'indigo', 'violet'}
print(rainbow_colors)
print(type(rainbow_colors))
empty_set = set()
print(type(empty_set))
nl = [1, 23, 45, 1, 56, 23, 34, 45]
t_tuple = ('a', 'v', 't', 'a', 'b', 'v', 't', 'a')
set_nl = set(nl)
set_t = set(t_tuple)
print(set_nl)
print(set_t)
set_t.discard('v')
# bool
# age = int(input('input your age...'))
print('access is permitted: ' + str(age >= 18), age)
# if/elif/else
x = 5
if x > 3:
    print('x > 3')
elif x < 3:
    print('x < 3')
else:
    print('x == 3')

day_time = 'midnight'
if day_time == 'morning':
    print('monster wakes up')
elif day_time == 'afternoon':
    print('monster walks')
elif day_time == 'evening':
    print('monster eats')
elif day_time == 'night':
    print('monster sleeps')
else:
    print('monster does something')

lucky_number = 3  # input('enter a number')
if lucky_number:
    print(str(lucky_number) + ' is your lucky number')
else:
    print('you have to enter number')
# forloop
number_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for number in number_list:
    if number % 2 == 0:
        print(number)
    else:
        print('boo')

num_sum = 0
for number in number_list:
    num_sum += number
print(num_sum)

some_str = 'njneqvbybwskmvlsekrnuiqbhvbdkn'
for letter in some_str:
    c = some_str.count(letter)
    # if letter == 'b':
    #     print(letter, end='')
    print(letter, c)

for item in car_prices.items():
    print(item)
for key, value in car_prices.items():
    print(key)
    print(value)
    print(key, value)

for _ in range(5):
    print('spam')
else:
    print('x not < 5')
# whileloop
while x >= 1:
    print(x)
    x -= 1

x = 0
while x < 10:
    print(' x < 10')
    x += 1
else:
    print('x not < 10')
# pass, break, continue
my_list = [1, 2, 3]
for item in my_list:
    pass
print('end')

for item in my_list:
    if item == 2:
        break
    print(item)
print('end')

for item in my_list:
    if item == 2:
        continue
    print(item)
print('end')
# range
for x in range(3, 7):
    print(x)
print(list(range(1, 6)))

my_string = 'abcdefg'
for item in enumerate(my_string):
    print(item)

