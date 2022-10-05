n = int(input('В какую систему конвертируем: '))
num = int(input('Введите число: '))
res_list = []

while num != 0:
    x = num % n
    if x >= 10:
        sym = chr(87 + x)
        res_list.insert(0, str(sym.upper()))
    else:
        res_list.insert(0, str(x))
    num = num // n

print(''.join(res_list))
