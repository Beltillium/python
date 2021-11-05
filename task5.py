def my_func(nums):
    sum_1 = 0
    for i in nums:
        sum_1 += int(i)
    return sum_1


print('Для остановки суммирования введите "t"')
sum2 = 0
trigger = True
while trigger:
    nums = input('Введите числа через пробел: ').split()
    if nums.count('t') != 0:
        nums.remove('t')
        trigger = False
    sum2 += my_func(nums)
    print(sum2)
