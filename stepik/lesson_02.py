# 7 => 100
a = int(input())
if a >= 2 and a <= 17:
    b = 3
    p = a * a + b * b
else:
    b = 5
p = (a + b) * (a + b)
print(p)
# Напишите программу, которая определяет, является ли заданное натуральное число трёхзначным.
num = int(input())
if 100 <= num <= 999:     # num >= 100 and num <= 999
    print('Число является трёхзначным')
else:
    print('Число не является трёхзначным')
# Напишите программу, которая проверяет, что все три цифры натурального трёхзначного числа различны.
num = int(input())
d3 = num % 10
d2 = num % 100 // 10
d1 = num // 100
if d3 != d2 and d3 != d1 and d2 != d1:
    print('Цифры различны')
else:
    print('Цифры не различны')
# Напишите программу, которая по координатам точки, не лежащей на осях координат,
# определяет номер координатной четверти, в которой она находится.
x = int(input())
y = int(input())
if x > 0 and y > 0:
    print('1 четверть')
if x < 0 < y:
    print('2 четверть')
if x < 0 and y < 0:
    print('3 четверть')
if x > 0 > y:
    print('4 четверть')
# Ход короля
x1, y1, x2, y2 = 4, 4, 2, 4
if -1 <= x2 - x1 <= 1 and -1 <= y2 - y1 <= 1:
    print('YES')
else:
    print('NO')
# пересечение отрезков
a1, b1, a2, b2 = int(input()), int(input()), int(input()), int(input())
if a2 > b1 or a1 > b2:
    print('пустое множество')
elif b2 >= b1:
    if b1 == a2:
        print(b1)
    elif a2 >= a1:
        print(a2, b1)
    elif a2 <= a1:
        print(a1, b1)
elif b1 >= b2:
    if b2 == a1:
        print(a1)
    elif a2 <= a1:
        print(a1, b2)
    elif a1 <= a2:
        print(a2, b2)
