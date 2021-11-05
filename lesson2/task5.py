my_list = [7, 5, 3, 3, 2]
a = int(input('Введите новый элемент рейтинга: '))
for i in range(len(my_list)):
    if a > my_list[i]:
        my_list.insert(i, a)
        print(my_list)
        break
    elif a == my_list[i] and a > my_list[i+1]:
        my_list.insert(i + 1, a)
        print(my_list)
        break
if my_list[len(my_list) - 1] > a:
    my_list.append(a)
    print(my_list)