def to_jaden_case(string):
    my_list = []
    for word in string.split():
        my_list.append(word.capitalize())

    return ' '.join(my_list)


print(to_jaden_case("How can mirrors be real if our eyes aren't real"))


def positive_sum(arr):
    p_sum = 0
    if arr:
        for num in arr:
            if num > 0:
                p_sum += num
        return p_sum


print(positive_sum([1, 2, 3, 4, 5]))
print(positive_sum([1, -2, 3, 4, 5]))
print(positive_sum([-1, 2, 3, 4, -5]))


def even_or_odd(number):
    return 'Even' if number % 2 == 0 else 'Odd'


print(even_or_odd(15))


def make_negative(number):
    return number if number < 0 else -number


print(make_negative(42))


def high_and_low(numbers):
    list_num = list(numbers.split())
    num = []
    for i in list_num:
        num.append(int(i))
    return f'{max(num)} {min(num)}'


print(high_and_low("8 3 -5 42 -1 0 0 -9 4 7 4 -4"))


def solution(string):
    return string[::-1]


print(solution('world'))


def no_space(x):
    new_list = []
    for c in x:
        if c != ' ':
            new_list += c
    return ''.join(new_list)


print(no_space('df g sgs  dsbf ssfe  agd ag z    '))


def get_sum(a, b):
    if a == b:
        return a
    else:
        min_x = min(a, b)
        max_x = max(a, b)
        x_sum = max_x
        for i in range(min_x, max_x):
            x_sum += i
    return x_sum


print(get_sum(-1, -3))
print(get_sum(-2434, -3909))


def remove_char(s):
    if len(s) > 1:
        s = list(s)
        s.pop(0)
        s.pop()
        return ''.join(s)
    else:
        return ''


print(remove_char('place'))
print(remove_char('ok'))
