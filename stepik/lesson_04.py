text = input()
total = 0
while text != 'stop':
    num = int(text)
    total += num
    text = input()
print('Сумма чисел равна', total)

n = int(input())
while n != 0:  # пока в числе есть цифры
    last_digit = n % 10  # получить последнюю цифру
    # код обработки последней цифры
    n = n // 10  # удалить последнюю цифру из числа

# Напишем программу, которая определяет есть ли в числе цифра 7.
num = int(input())
has_seven = False  # сигнальная метка
while num != 0:
    last_digit = num % 10
    if last_digit == 7:
        has_seven = True
    num = num // 10
if has_seven:
    print('YES')
else:
    print('NO')
# -----
num = 12345
product = 1
while num != 0:
    last_digit = num % 10
    product = product * last_digit
    num = num // 10
print(product)  # =120
# -----
num = 123456789
total = 0
while num != 0:
    last_digit = num % 10
    if last_digit > 4:
        total += 1
    num = num // 10
print(total)  # =5
# min/max
num = int(input())
last_digit = num % 10
small, large = last_digit, last_digit
while num != 0:
    last_digit = num % 10
    if last_digit > large:
        large = last_digit
    if last_digit < small:
        small = last_digit
    num = num // 10
print(f'Максимальная цифра равна {large}')
print(f'Минимальная цифра равна {small}')
# Дано натуральное число. Напишите программу, которая вычисляет:
# сумму его цифр;
# количество цифр в нем;
# произведение его цифр;
# среднее арифметическое его цифр;
# его первую цифру;
# сумму его первой и последней цифры.
num = int(input())
total = 0
counter = 0
total_m = 1
last = num % 10
num_copy = num
while num != 0:
    last_digit = num % 10
    total += last_digit
    counter += 1
    total_m *= last_digit
    num = num // 10
first = num_copy // 10 ** (counter - 1)
print(total)
print(counter)
print(total_m)
print(total / counter)
print(first)
print(first + last)
# Дано натуральное число n(n>9). Напишите программу, которая определяет его вторую (с начала) цифру.
num = int(input())
second = num % 10
while num != 0:
    last = num % 10
    second, last = last, second
    num = num // 10
print(last)
# или:
num = int(input())
second = num % 10
while num > 0:
    last = num % 10
    num = num // 10
    second = last
print(second)
# Напишите программу, которая определяет, является ли последовательность его цифр при просмотре
# справа налево упорядоченной по неубыванию.
num = int(input())
first = num % 10
flag = 'YES'
while num != 0:
    last_digit = num % 10
    if last_digit < first:
        flag = 'NO'
    num = num // 10
    first = last_digit
print(flag)
# break
num = int(input())
flag = True
for i in range(2, num):
    if num % i == 0:        # если исходное число делится на какое-либо отличное от 1 и самого себя
        flag = False
        break               # останавливаем цикл если встретили делитель числа
if flag:
    print('Число простое')
else:
    print('Число составное')
# Напишите программу, которая печатает равнобедренный звездный треугольник с основанием, равным n
# в соответствии с примером:
# *
# **
# ***
# ****
# ***
# **
# *
n = int(input())
for i in range(1, n // 2 + 1):
    for j in range(i):
        print('*', end='')
    print()
for i in range(n // 2 + 1, 0, -1):
    for j in range(i):
        print('*', end='')
    print()
# Найдите все пары натуральных чисел (и их количество) являющихся решением уравнения 12x+13y=777
total = 0
for x in range(1, 65):
    for y in range(1, 60):
        if 12 * x + 13 * y == 777:
            total += 1
            print('x =', x, 'y =', y)
print('Общее количество натуральных решений =', total)
# 3 неизвестных
total = 0
for x in range(1, 13):
    for y in range(1, 12):
        for z in range(1, 11):
            if 28 * x + 30 * y + 31 * z == 365:
                total += 1
                print('x =', x, 'y =', y, 'z =', z)
print('Общее количество натуральных решений =', total)
# Найдите все пары натуральных чисел (и их количество) являющихся решением уравнения x^2+y^2+z^2=2020
total = 0
for x in range(1, 45):
    for y in range(1, 45):
        for z in range(1, 45):
            if x ** 2 + y ** 2 + z ** 2 == 2020:
                total += 1
                print('x =', x, 'y =', y, 'z =', z)
print('Общее количество натуральных решений =', total)
# Гипотеза Эйлера о сумме степеней
total = 0
for a in range(1, 150):
    for b in range(a, 150):
        for c in range(b, 150):
            for d in range(c, 150):
                for e in range(d, 150):
                    if a**5 + b**5 + c**5 + d**5 == e**5:
                        total += 1
                        print('a =', a, 'b =', b, 'c =', c, 'd =', d, 'e =', e)
                        print(a + b + c + d + e)
print('Общее количество натуральных решений =', total)
# ответ:
# a = 27 b = 84 c = 110 d = 133 e = 144
# 498

# --------------------------------------
# На вход программе подается два натуральных числа a и b (a< b). Напишите программу, которая находит
# натуральное число из отрезка [a;b] с максимальной суммой делителей.
a, b = 61, 71
max_total = 0
max_num = 0
for i in range(a, b + 1):
    count = 0
    total = 0
    for j in range(1, i + 1):
        if i % j == 0:
            total += j
    if total >= max_total:
        max_total = total
        max_num = i
print(max_num, max_total)
# На вход программе подается натуральное число n. Напишите программу, выводящую графическое изображение делимости
# чисел от 1 до n включительно. В каждой строке надо напечатать очередное число и столько символов «+»,
# сколько делителей у этого числа.
n = 5
for i in range(1, n + 1):
    total = 0
    for j in range(1, i + 1):
        if i % j == 0:
            total += 1
    print(str(i) + ('+' * total))
# Сумма факториалов
n = 10
total = 0
for i in range(1, n + 1):
    prod = 1
    for j in range(1, i + 1):
        prod *= j
    total += prod
print(total)
# На вход программе подается два натуральных числа a и b (a< b). Напишите программу, которая находит
# все простые числа от a до b включительно.
a, b = 1, 5
for i in range(a, b + 1):
    is_prime = True
    if i < 2:
        continue
    for j in range(2, i):
        if i % j == 0:
            is_prime = False
    if is_prime:
        print(i)
# Дано натуральное число. Напишите программу, которая вычисляет:
#
# количество цифр 3 в нем;
# сколько раз в нем встречается последняя цифра;
# количество четных цифр;
# сумму его цифр, больших пяти;
# произведение цифр, больших семи (если цифр больших семи нет, то вывести 1, если такая цифра одна, то вывести ее);
# сколько раз в нем встречается цифры 0 и 5 (всего суммарно).
n = 56689932106
counter3 = 0
_last = n % 10
count_last = 0
count_even = 0
total5 = 0
total7 = 1
count7 = 0
counter0_5 = 0
while n != 0:
    last = n % 10
    if last == 3:
        counter3 += 1
    if last == _last:
        count_last += 1
    if last % 2 == 0:
        count_even += 1
    if last > 5:
        total5 += last
    if last > 7:
        total7 *= last
        count7 += 1
    if last == 0 or last == 5:
        counter0_5 += 1
    n //= 10
print(counter3)
print(count_last)
print(count_even)
print(total5)
print('1' if count7 == 0 else total7)
print(counter0_5)
# Числа Рамануджана
total = 0
for x in range(1, 33):
    for y in range(1, 33):
        for a in range(1, 33):
            for b in range(1, 33):
                if x ** 3 + y ** 3 == a ** 3 + b ** 3 and x != b and y != a and y != b and x > y and b < a < x:
                    total += 1
                    print('x =', x, 'y =', y, 'a =', a, 'b =', b)
                    print(x ** 3 + y ** 3)
print('Общее количество натуральных решений =', total)
