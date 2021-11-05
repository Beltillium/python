def my_func(num1, num2, num3):
    sum1 = num1 + num2
    sum2 = num2 + num3
    sum3 = num1 + num3
    print(max(sum1, sum2, sum3))


a = int(input('Введите первое число: '))
b = int(input('Введите второе число: '))
c = int(input('Введите третье число: '))
my_func(a, b, c)
