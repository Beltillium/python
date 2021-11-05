def divis(arg1, arg2):
    if arg2 == 0:
        print('Деление на 0 невозможно')
    else:
        print(arg1 / arg2)


a = int(input('Введите делимое: '))
b = int(input('Введите делитель: '))
divis(a, b)