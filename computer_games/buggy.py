import random

number1 = random.randint(1, 10)
number2 = random.randint(1, 10)
print('сколько будет: ' + str(number1) + ' + ' + str(number2) + '?')
answer = input()
if int(answer) == number1 + number2:
    print('Верно!')
else:
    print('Нет! Правильный ответ: ' + str(number1 + number2))
