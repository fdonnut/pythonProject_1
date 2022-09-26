# Напишите программу, определяющую число десятков и единиц в двузначном числе.
num = int(input())
last_digit = num % 10
first_digit = num // 10
print('Число десятков =', first_digit)
print('Число единиц =', last_digit)
# Напишите программу, в которой рассчитывается сумма цифр двузначного числа.
num = int(input())
last_digit = num % 10
first_digit = num // 10
print('Сумма цифр =', last_digit + first_digit)
# Напишите программу, которая печатает число, образованное при перестановке цифр двузначного числа.
num = int(input())
last_digit = num % 10
first_digit = num // 10
print('Искомое число =', last_digit * 10 + first_digit)
# Напишите программу, в которую вводится трёхзначное число и выводит на экран его цифры (через запятую).
num = int(input())
digit3 = num % 10
digit2 = (num // 10) % 10
digit1 = num // 100
print(digit1, digit2, digit3, sep=',')
# Напишите программу для нахождения цифр четырёхзначного числа.
num = int(input())
print(f'Цифра в позиции тысяч равна {num // 1000}')  # n % 10000 // 1000
print(f'Цифра в позиции сотен равна {(num // 100) % 10}')  # n % 1000 // 100
print(f'Цифра в позиции десятков равна {(num // 10) % 10}')  # n % 100 // 10
print(f'Цифра в позиции единиц равна {num % 10}')
# Напишите программу, которая считывает два целых числа a и b и выводит на экран квадрат суммы и сумму квадратов.
a, b = int(input()), int(input())
print(f'Квадрат суммы {a} и {b} равен {(a + b) ** 2}')
print(f'Сумма квадратов {a} и {b} равна {a ** 2 + b ** 2}')
# Напишите программу, которая считывает четыре целых положительных числа a, b, c и d и выводит на экран
# значение выражения a^b + c^d
a, b, c, d = int(input()), int(input()), int(input()), int(input())
print(a ** b + c ** d)
# Напишите программу, которая считывает целое положительное число n, n in [1:9] и выводит значение числа n+nn+nnn
n = input()
print(int(n) + int(n + n) + int(n + n + n))
# Напишите программу, которая определяет, состоит ли двузначное число, введенное с клавиатуры, из одинаковых цифр.
# Если состоит, то программа выводит «ДА», в противном случае программа выводит «НЕТ»
num = int(input())
last_digit = num % 10    # последняя цифра числа
first_digit = num // 10  # первая цифра числа
if last_digit == first_digit:
    print('ДА')
else:
    print('НЕТ')
# Напишите программу, которая считывает три числа и подсчитывает количество чётных чисел.
num1, num2, num3 = int(input()), int(input()), int(input())
counter = 0  # переменная счётчик
if num1 % 2 == 0:
    counter = counter + 1  # увеличиваем счётчик на 1
if num2 % 2 == 0:
    counter = counter + 1  # увеличиваем счётчик на 1
if num3 % 2 == 0:
    counter = counter + 1  # увеличиваем счётчик на 1
print(counter)