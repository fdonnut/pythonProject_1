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
