import random


def get_random_numbers(loto_num_1, loto_num_2):
    i = 0
    nums = []
    while i < loto_num_1:
        num = random.randint(1, loto_num_2)
        if num not in nums:
            nums.append(num)
            i = i + 1
    return nums


print('"4 из 20", выиграют номера:', get_random_numbers(4, 20), get_random_numbers(4, 20))
print('"6 из 45", выиграют номера:', get_random_numbers(6, 45))
print('"5 из 36", выиграют номера:', get_random_numbers(5, 36), get_random_numbers(1, 4))
print('"Большое Спортлото", выиграют номера:', get_random_numbers(5, 50), get_random_numbers(2, 10))

for _ in range(23):
    lucky = get_random_numbers(6, 45)
print(lucky)