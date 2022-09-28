# Напишите программу, которая упорядочивает три числа от большего к меньшему.
a, b, c = int(input()), int(input()), int(input())
print(max(a, b, c))
print((a + b + c) - max(a, b, c) - min(a, b, c))
print(min(a, b, c))
# Даны названия трех городов. Напишите программу, которая определяет самое короткое и самое длинное название города.
a, b, c = input(), input(), input()
min_len = min(len(a), len(b), len(c))
max_len = max(len(a), len(b), len(c))
if len(a) == min_len:
    print(a)
elif len(b) == min_len:
    print(b)
else:
    print(c)
if len(a) == max_len:
    print(a)
elif len(b) == max_len:
    print(b)
else:
    print(c)
# решение
a, b, c = input(), input(), input()
if len(a) < len(b): b, a = a, b
if len(c) > len(b): c, b = b, c
if len(c) > len(a): c, a = a, c
print(c, a, sep='\n')
# Вводятся 3 строки в случайном порядке. Напишите программу, которая выясняет можно ли из длин этих строк построить
# возрастающую арифметическую прогрессию.
a = len(input())
b = len(input())
c = len(input())
max_len = max(a, b, c)
min_len = min(a, b, c)
if max_len - ((a + b + c) - max_len - min_len) == ((a + b + c) - max_len - min_len) - min_len:
    print('YES')
else:
    print('NO')
# Квадратное уравнение
a, b, c = float(input()), float(input()), float(input())
d = b ** 2 - 4 * a * c
if d < 0:
    print('Нет корней')
elif d == 0:
    print(-b / (2 * a))
else:
    x1 = (-b + d ** 0.5) / (2 * a)
    x2 = (-b - d ** 0.5) / (2 * a)
    print(min(x1, x2))
    print(max(x1, x2))
# На вход программе подается три натуральных числа m,p,n:
# m: стартовое количество организмов;
# p: среднесуточное увеличение в %;
# n: количество дней для размножения.
# Напишите программу, которая предсказывает размер популяции организмов.
# Программа должна выводить размер популяции в каждый день, начиная с 1 и заканчивая n-м днем.
m, p, n = float(input()), float(input()), int(input())
for i in range(n):
    print(i + 1, m)
    m = m + m * p / 100
