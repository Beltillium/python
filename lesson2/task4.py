my_list = [str(i) for i in input('Введите слова, разделенные пробелами: ').split()]
print(my_list)
for i in range(len(my_list)):
    print(i + 1, f'{my_list[i][0:10]}')
