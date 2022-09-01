# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# print('2^10=', 2 ** 10)
# user_input = input('Введите координаты цели: ')
# print(type(user_input))
# x, y, = map(int, input().split())
# print(type(x))
# print(x, y)

my_list = [1, 2, 'my_list', 4, 5]
print(my_list)
my_list.append(77)
my_list.insert(3, 'super')
my_list.remove('my_list')
print(my_list)
print('super' in my_list)
# print(list(range(10)))
my_list.extend([3, 7, 9, 4, 3])
my_list.remove('super')
print(my_list)
print(min(my_list), max(my_list))
my_list.sort()
print(my_list)
valve = 42
mass = valve
print(valve, id(valve), mass, id(mass))
mass += 1
print(valve, id(valve), mass, id(mass))
