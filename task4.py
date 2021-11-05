def my_func(arg1, arg2):
    print('Решение 1:', arg1 ** arg2)
    result2 = 1
    for i in range(arg2):
        result2 *= arg1
    print('Решение 2:', result2)


x = int(input('Введите число возводимое в степень: '))
y = int(input('Введите степень: '))
my_func(x, y)