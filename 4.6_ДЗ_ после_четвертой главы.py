# Домашнее задание:
print('Домашнее задание:')



# 1. Напишите функцию (F): на вход список имен и целое число N;
# на выходе список длины N случайных имен из первого списка (могут повторяться,
# можно взять значения: количество имен 20, N = 100, рекомендуется использовать функцию random);
print(' Создал список name_list  с именами ')

name_list = ['Ваня', 'Зина', 'Артур', 'Илья', 'Семен', 'Просковья','Маргарита', 'Альберт', 'Фрэнк', 'Артем',
             'Дмитрий', 'София', 'Ева', 'Ромео', 'Джульетта', 'Фокс', 'Карбофос', 'Фунтик', 'Том', 'Джери']
print('Всего слов в name_list: ',len(name_list))

print()

import random
def rnd_name(name_list, z):
    ''''

    name_list = список имен
    z = к длина созданой последовательности

    Функция создает случайную последоательность из элементов
    в списке name_list, длиой равной к

    '''

    rnd_list = random.choices(name_list, k=z)
    print(rnd_list)
    print('Всего имен в списке: ', len(rnd_list))
    return rnd_list

rnd_name(['Ваня', 'Зина', 'Артур', 'Илья', 'Семен', 'Просковья','Маргарита', 'Альберт', 'Фрэнк', 'Артем',
             'Дмитрий', 'София', 'Ева', 'Ромео', 'Джульетта', 'Фокс', 'Карбофос', 'Фунтик', 'Том', 'Джери'], z=100)

print('  *  *  *  ')





# 2. Напишите функцию вывода самого частого имени из списка на выходе функции F;




# 3. Напишите функцию вывода самой редкой буквы, с которого начинаются имена в списке на выходе функции F.


