a = int(input('Введите количество товара: '))
my_dict = []
my_list = []
analytics = {}
n = 1
while n <= a:
    my_dict = dict({'название': input('Введите название: '), 'цена': input('Введите цену: '),
                    'количество': input('Введите количество: '), 'ед. изм': input('Введите единицу измерения: ')})
    my_list.append((n, my_dict))
    n += 1
    # ?
    analytics = dict(
        {'название': [analytics.get('название'), my_dict.get('название')],
         'цена': [analytics.get('цена'), my_dict.get('цена')],
         'количество': [analytics.get('количество'), my_dict.get('количество')],
         'ед. изм': [analytics.get('ед. изм'), my_dict.get('ед. изм')]})
    # ?
for i in range(a):
    print(my_list[i])
print(analytics)  # ?
