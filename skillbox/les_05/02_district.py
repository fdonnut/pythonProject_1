# -*- coding: utf-8 -*-

# Составить список всех живущих на районе и Вывести на консоль через запятую
# Формат вывода: На районе живут ...
# подсказка: для вывода элементов списка через запятую можно использовать функцию строки .join()
# https://docs.python.org/3/library/stdtypes.html#str.join

from district.central_street.house1 import room1, room2

people = room1.folks[:]
people += room2.folks[:]

from district.central_street.house2 import room1, room2

people += room1.folks[:]
people += room2.folks[:]

from district.soviet_street.house1 import room1, room2

people += room1.folks[:]
people += room2.folks[:]

from district.soviet_street.house2 import room1, room2

people += room1.folks[:]
people += room2.folks[:]

print(', '.join(people))
