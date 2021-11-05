my_list = [str(i) for i in input('Введите значения через пробел: ').split()]
print(my_list)
c = len(my_list)
if c % 2 == 1:
    c -= 1
for n in range(0, c, 2):
    my_list[n], my_list[n+1] = my_list[n+1], my_list[n]
print(my_list)
