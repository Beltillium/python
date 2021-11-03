month = int(input('Введите месяц в числовом формате (от 1 до 12): '))
d = {1: 'Зима', 2: 'Весна', 3: 'Лето', 4: 'Осень'}
solution_2 = [0, 'Зима', 'Весна', 'Лето', 'Осень']
if month == 1 or month == 2 or month == 12:
    print(d[1], solution_2[1])
elif 2 < month < 6:
    print(d[2], solution_2[2])
elif 5 < month < 9:
    print(d[3], solution_2[3])
else:
    print(d[4], solution_2[4])