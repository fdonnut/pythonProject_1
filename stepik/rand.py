import random

# n = int(input())    # количество попыток
# for _ in range(n):
#     print('Орел' if random.randint(0, 1) == 1 else 'Решка')
#
# for _ in range(n):
#     print(random.randint(1, 6))
#
# length = int(input())
# for _ in range(length):
#     if random.randint(0, 1) == 1:
#         print(chr(random.randint(65, 90)), end='')
#     else:
#         print(chr(random.randint(97, 122)), end='')
# print()
#
# nums = set()
# while len(nums) != 7:
#     nums.add(random.randint(1, 49))
# print(*sorted(nums))


def generate_ip():
    s = []
    for _ in range(4):
        s.append(str(random.randint(0, 255)))
    return '.'.join(s)


print(generate_ip())


def generate_index():
    ind = ''
    ind += chr(random.randint(65, 90))
    ind += chr(random.randint(65, 90))
    ind += str(random.randint(0, 99))
    ind += '_'
    ind += str(random.randint(0, 99))
    ind += chr(random.randint(65, 90))
    ind += chr(random.randint(65, 90))
    return ind


print(generate_index())


matrix = [[1, 2, 3, 4],
          [5, 6, 7, 8],
          [9, 10, 11, 12],
          [13, 14, 15, 16]]
for i in range(len(matrix)):
    random.shuffle(matrix[i])
random.shuffle(matrix)
print(matrix)
matrix = [[1, 2, 3, 4],
          [5, 6, 7, 8],
          [9, 10, 11, 12],
          [13, 14, 15, 16]]

n, m, lst = len(matrix), len(matrix[0]), sum(matrix, [])
random.shuffle(lst)
matrix = [[lst[i * m + j] for j in range(m)] for i in range(n)]
print(matrix)

nums = set()
while len(nums) != 100:
    nums.add(random.randint(1000000, 9999999))
print(*nums, sep='\n')

s = 'липа'
print(''.join(random.sample(s, len(s))))

num = random.sample([i for i in range(76)], 25)
num[12] = 0
temp = []
for i in range(0, len(num), 5):
    temp.append(num[i: i + 5])
for x in temp:
    for y in x:
        print(str(y).ljust(3), end='')
    print()

# montecarlo
n = 10**6       # количество испытаний

k = 0
s0 = 4
for _ in range(n):
    x = random.uniform(-1, 1)
    y = random.uniform(-1, 1)

    if x**2 + y**2 < 1:
        k += 1

print((k/n)*s0)
