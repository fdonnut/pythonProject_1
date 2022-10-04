import random
n = random.randint(1, 100)
count = 0
print('Добро пожаловать в числовую угадайку')


def is_valid(num):
    return num.isdigit() and 0 < int(num) < 101


while True:
    number = input('Ваше число...')
    if not is_valid(number):
        print('А может быть все-таки введем целое число от 1 до 100?')
        continue
    number = int(number)

    if number < n:
        print('Ваше число меньше загаданного, попробуйте еще разок')
        count += 1

    if number > n:
        print('Ваше число больше загаданного, попробуйте еще разок')
        count += 1

    if number == n:
        print(f'Вы угадали за {count + 1} попытки, поздравляем! ')
        break

print('Спасибо, что играли в числовую угадайку. Еще увидимся...')
