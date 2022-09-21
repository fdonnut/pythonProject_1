# funcs
def print_hello(name='noname'):
    print('hello ' + name)


print_hello('bob')
print_hello()


def sum_a_b(a=0, b=0):
    return a + b


print(sum_a_b(3495, 4238))
print(sum_a_b())


def is_hello_in_text(text):
    # if 'hello' in text.lower():
    #     return True
    # else:
    #     return False
    return 'hello' in text.lower()


print(is_hello_in_text('say hello everyone'))


def is_string_in_text(string, text):
    return string in text


print(is_string_in_text('be', 'hello'))


def greet_depends_on_gender(name, gender):
    if gender == 'male':
        print('hello ' + name + '! you look great!')
        return gender
    elif gender == 'female':
        print('hello ' + name + '! you are nice!')
        return gender
    else:
        print('hello ' + name + '! i\'ve never seen the creature like you!')
        return gender


greet_depends_on_gender('jack', 'male')
greet_depends_on_gender('jane', 'female')
greet_depends_on_gender('ja', 'cmale')


# *args, **kwargs
def percent(per, *args):
    m = 1
    for num in args:
        m *= num
    return m / 100 * per


print(percent(5, 10, 20, 5))


def func_kwargs(**kwargs):
    print(kwargs)


func_kwargs(first=1, second=2, third=3)


def hello(hello, **kwargs):
    if 'name' in kwargs:
        print('{}, nice to meet you, {} {}'.format(hello, kwargs['name'], kwargs['age']))
    else:
        print('{}! what is your name?'.format(hello))


hello('hi', gender='male', age=24, name='jack')
hello('hello')


def func_args_kwargs(*args, **kwargs):
    print(args)
    print(kwargs)
    print("i'd like {} {}".format(args[0], kwargs['food']))


func_args_kwargs('one', 'two', drink='coffee', food='burger')


# map
def sum_num(x):
    return x + x


num_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]

result = map(sum_num, num_list)

for item in result:
    print(item)

for item in map(sum_num, num_list):
    print(item)

print(list(map(sum_num, num_list)))


def is_a_in_string(string):
    if 'a' in string:
        print('string has "a"')
        return True
    else:
        print('string has not "a"')
        return False


string_list = ['hi', 'was', 'name', 'he']

print(list(map(is_a_in_string, string_list)))


# filter
def is_number_odd(number):
    return number % 2 == 1


num_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]

print(list(filter(is_number_odd, num_list)))

for number in filter(is_number_odd, num_list):
    print(number)


# lambda
def cube(num):
    return num ** 3


num_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]

print(list(map(cube, num_list)))

print(list(map(lambda num: num ** 3, num_list)))

# scope
# pi = 'outer pi variable'
#
#
# def print_pi():
#     pi = 'inner pi variable'
#     print(pi)
#
#
# print_pi()
# print(pi)

# enclosed scope
pi = 'global pi variable'


def outer():
    pi = 'outer pi variable'

    def inner():
        # pi = 'inner pi variable'
        nonlocal pi
        print(pi)

    inner()


outer()
print(pi)

# built-in scope
from math import pi

# pi = 'global pi'


def outer():
    # pi = 'outer pi'

    def inner():
        # pi = 'inner pi'
        print(pi)

    inner()


outer()
