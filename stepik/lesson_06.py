# Алгоритмы сортировки
# алгоритм пузырьковой сортировки
a = [17, 24, 91, 96, 67, -27, 79, -71, -71, 58, 48, 88, 88, -16, -78, 96, -76, 56, 92, 1, 32, -17, 36, 88, -61, -97,
     -37, -84, 50, 47, 94, -6, 52, -76, 93, 14, -32, 98, -65, -16, -9, -68, -20, -40, -71, 93, -91, 44, 25, 79, 97,
     0, -94, 7, -47, -96, -55, -58, -78, -78, -79, 75, 44, -56, -41, 38, 16, 70, 17, -17, -24, -83, -74, -73, 11,
     -26, 63, -75, -19, -13, -51, -74, 21, -8, 21, -68, -66, -84, -95, 78, 69, -29, 39, 38, -55, 7, -11, -26, -62, -84]

n = len(a)

for i in range(n - 1):
    for j in range(n - i - 1):
        if a[j] > a[j + 1]:
            a[j], a[j + 1] = a[j + 1], a[j]

print(a)
# сортировка выбором
a = [78, -32, 5, 39, 58, -5, -63, 57, 72, 9, 53, -1, 63, -97, -21, -94, -47, 57, -8, 60, -23, -72, -22, -79, 90, 96,
     -41, -71, -48, 84, 89, -96, 41, -16, 94, -60, -64, -39, 60, -14, -62, -19, -3, 32, 98, 14, 43, 3, -56, 71, -71,
     -67, 80, 27, 92, 92, -64, 0, -77, 2, -26, 41, 3, -31, 48, 39, 20, -30, 35, 32, -58, 2, 63, 64, 66, 62, 82, -62, 9,
     -52, 35, -61, 87, 78, 93, -42, 87, -72, -10, -36, 61, -16, 59, 59, 22, -24, -67, 76, -94, 59]

n = len(a)

for i in range(n):
    small_ind = i
    for j in range(i + 1, n):
        if a[j] < a[small_ind]:
            small_ind = j
    a[i], a[small_ind] = a[small_ind], a[i]

print(a)
# сортировка простыми вставками
a = [1, 7, -3, 9, 0, -67, 34, 12, 45, 1000, 6,  8, -2, 99]
n = len(a)

for i in range(1, n):
    elem = a[i]  # первый элемент из неотсортированной части списка
    j = i
    while j >= 1 and a[j - 1] > elem:
        a[j] = a[j - 1]
        j -= 1
    a[j] = elem

print('Отсортированный список:', a)


# гипотенуза
def compute_hypotenuse(a, b):
    c = (a ** 2 + b ** 2) ** 0.5
    return c


print(compute_hypotenuse(5, 6))

# На вход программе подается число nn, а затем nn строк, содержащих целые числа в порядке возрастания.
# Из данных строк формируются списки чисел. Напишите программу, которая объединяет указанные списки в один
# отсортированный список с помощью функции quick_merge(), а затем выводит его.
def quick_merge(list1, list2):
    result = []

    p1 = 0  # указатель на первый элемент списка list1
    p2 = 0  # указатель на первый элемент списка list2

    while p1 < len(list1) and p2 < len(list2):  # пока не закончился хотя бы один список
        if list1[p1] <= list2[p2]:
            result.append(list1[p1])
            p1 += 1
        else:
            result.append(list2[p2])
            p2 += 1

    if p1 < len(list1):  # прицепление остатка
        result += list1[p1:]
    if p2 < len(list2):
        result += list2[p2:]

    return result


total_list = []
for i in range(int(input())):
    num = [int(q) for q in input().split()]
    total_list = quick_merge(total_list, num)
print(*total_list)


# BEEGEEK наконец открыл свой банк в котором используются специальные банкоматы с необычным паролем.
#
# Действительный пароль BEEGEEK банка имеет вид a:b:c, где a, b и c – натуральные числа. Поскольку основатель
# BEEGEEK фанатеет от математики, то он решил:
#
# число a – должно быть палиндромом;
# число b – должно быть простым;
# число c – должно быть четным.
# Напишите функцию is_valid_password(password), которая принимает в качестве аргумента строковое значение пароля
# password и возвращает значение True если пароль является действительным паролем BEEGEEK банка и False в
# противном случае.
def is_palindrome(text):
    return text[:] == text[::-1]

def is_prime(num):
    return len([x for x in range(1, int(num) + 1) if int(num) % x == 0]) == 2

def is_even(num):
    return int(num) % 2 == 0


def is_valid_password(password):
    password = list(password.split(':'))
    if len(password) > 3:
        return False
    return is_palindrome(password[0]) and is_prime(password[1]) and is_even(password[2])


# считываем данные
psw = '15551:7:290'

# вызываем функцию
print(is_valid_password(psw))

# Напишите функцию is_correct_bracket(text), которая принимает в качестве аргумента непустую строку text,
# состоящую из символов ( и ) и возвращает значение True если поступившая на вход строка является правильной
# скобочной последовательностью и False в противном случае.
def is_correct_bracket(text):
    while '()' in text:
        text = text.replace('()', '')
        print(text)
    return len(text) == 0

# считываем данные
txt = '())((((())))'

# вызываем функцию
print(is_correct_bracket(txt))

# snake_case
def convert_to_python_case(text):
    lst = []
    i = 1
    lst.append(text[0].lower())
    while i < len(text):
        if text[i].isupper():
            lst.append('_')
        lst.append(text[i].lower())
        i += 1
    return ''.join(lst)


# считываем данные
txt = 'MyMethodThatDoSomething'

# вызываем функцию
print(convert_to_python_case(txt))

#        *
#       ***
#      *****
#     *******
#    *********
#   ***********
#  *************
# ***************
def draw_triangle():
    n = 8
    for i in range(n):
        print(' ' * (n - 1 - i) + '*' * (1 + i * 2))

# основная программа
draw_triangle()

# Напишите функцию number_to_words(num), которая принимает в качестве аргумента натуральное число num и
# возвращает его словесное описание на русском языке.
def number_to_words(num):
    lst = ['один', 'два', 'три', 'четыре', 'пять', 'шесть', 'семь', 'восемь', 'девять', 'десять', 'одиннадцать',
           'двенадцать', 'тринадцать', 'четырнадцать', 'пятнадцать', 'шестнадцать', 'семнадцать', 'восемнадцать',
           'девятнадцать', 'двадцать', 'тридцать', 'сорок', 'пятьдесят', 'шестьдесят', 'семьдесят', 'восемьдесят',
           'девяносто', '']
    if 0 < num <= 20:
        return lst[num - 1]
    elif 20 < num < 100:
        return ''.join(lst[num // 10 + 17] + ' ' + lst[num % 10 - 1].rstrip())


# считываем данные
n = 31

# вызываем функцию
print(number_to_words(n))

#Напишите функцию get_month(language, number), которая принимает на вход два аргумента language – язык ru или en
# и number – номер месяца (от 1 до 12) и возвращает название месяца на русском или английском языке.
def get_month(language, number):
    en = ['', 'january', 'february', 'march', 'april', 'may', 'june', 'july', 'august', 'september', 'october',
          'november', 'december']

    ru = ['', 'январь', 'февраль', 'март', 'апрель', 'май', 'июнь', 'июль', 'август', 'сентябрь', 'октябрь', 'ноябрь',
          'декабрь']
    return ru[number] if language == 'ru' else en[number]

# считываем данные
lan = 'en'
num = 12

# вызываем функцию
print(get_month(lan, num))

# Магическая дата – это дата, когда день, умноженный на месяц, равен числу образованному последними двумя цифрами года.
#
# Напишите функцию, is_magic(date) которая принимает в качестве аргумента строковое представление корректой даты и
# возвращает значение True если дата является магической и False в противном случае.
def is_magic(date):
    lst = date.split('.')
    return int(lst[0]) * int(lst[1]) == int(lst[2]) % 100

# считываем данные
date = '10.06.1960'

# вызываем функцию
print(is_magic(date))

# Панграмма – это фраза, содержащая в себе все буквы алфавита. Обычно панграммы используют для презентации шрифтов,
# чтобы можно было в одной фразе рассмотреть все глифы.
# Напишите функцию, is_pangram(text) которая принимает в качестве аргумента строку текста на английском языке и
# возвращает значение True если текст является панграммой и False в противном случае.
def is_pangram(text):
    abc = "abcdefghijklmnopqrstuvwxyz"
    for c in abc:
        if c not in text.lower():
            return False
    return True

# считываем данные
text = 'The jay pig fox zebra and my wolves quack'

# вызываем функцию
print(is_pangram(text))