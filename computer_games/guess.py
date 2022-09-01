import random

guessesTaken = 0

print('Привет! Как тебя зовут?')
myName = input()

number = random.randint(1, 20)
print('И так, ' + myName + ', я загадываю число от 1 до 20.')

for guessesTaken in range(6):
    print('Попробуй угадать.')
    guess = input()
    guess = int(guess)

    if guess < number:
        print('Твое число меньше загаданного.')

    if guess > number:
        print('Твое число больше загаданного.')

    if guess == number:
        break

if guess == number:
    guessesTaken = str(guessesTaken + 1)
    print('Отлично, ' + myName + '! Ты справился за ' + guessesTaken + ' попытки!')

if guess != number:
    number = str(number)
    print('Загаданное число ' + number + '.')
