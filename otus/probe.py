from functools import reduce
from functools import wraps
from contextlib import contextmanager

values = [2, 3, 4, 5, 6, 7, 8]


def fib(n):
    result = []
    a, b = 0, 1
    while a < n:
        result.append(a)
        a, b = b, a + b
    return result


def recur_fib(n):
    if n <= 1:
        return n
    return recur_fib(n - 1) + recur_fib(n - 2)


def exp(x):
    return lambda y: y ** x


def gen():
    for i in range(10):
        print(i)
        if i > 5:
            return
        yield i


g = gen()
print(list(g))
print(fib(100))
print(recur_fib(10))
exp_3 = exp(3)
print(exp_3(2))

mapped = map(lambda x: x + 3, values)
print(list(mapped))
c = 2
funcs = (exp(x) for x in range(2, 6))
print(list(map(lambda f: f(c), funcs)))
my_nums = range(-10, 20, 3)
print(list(filter(lambda x: -7 < x < 10, my_nums)))
to_mul = range(1, 7)
product = reduce(lambda x, y: x * y, to_mul, 10)
print(product)


def a_func():
    print('Hello from a_func!')


def decorator(func):
    def wrapper(*args, **kwargs):
        print(args)
        print(kwargs)
        return func(*args, **kwargs)

    return wrapper


@decorator
def count(a, b):
    return a + b


@decorator
def another_func():
    print('another func')


print(count(3, 4))
print(count(a=7, b=5))
print(count(27, b=10))
a_func()
a_func = decorator(a_func)
a_func()
a_func()
another_func()


def gen_dec(x):
    print('In a gen dec')

    def decorator_(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            print(args, kwargs)
            return func(x, *args, **kwargs)

        print('Generated a wrapper')
        return wrapper

    print('Generated a decorator')
    return decorator_


@gen_dec(50)
def mul(z, a, b):
    print(z, a, b)
    return z + a * b


print(mul(3, 4))


@contextmanager
def managed_res(*args, **kwargs):
    print(args, kwargs)
    yield map(lambda x: x * 2, args)
    print('closed', args)


with managed_res(1, 2, 3) as g:
    print(list(g))
    print('leaving')


print('left')
