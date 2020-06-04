# Предчистовик домашка со всеми промежуточными шагами и печатями

# 1. Напишите функцию (F): на вход список имен и целое число N;
# на выходе список длины N случайных имен из первого списка (могут повторяться,
# можно взять значения: количество имен 20, N = 100, рекомендуется использовать функцию random);

sps_list = (['Зина', 'Артур', 'Илья', 'Семен', 'Просковья','Маргарита', 'Альберт', 'Просковья','Фрэнк', 'Артем',
             'Дмитрий', 'София', 'Ева', 'Ромео', 'Джульетта', 'Фокс', 'Карбофос', 'Фунтик', 'Том', 'Джери'])
print('Количество имен в sps_list: ', len(sps_list))

print('       1. Напишите функцию (F): на вход список имен и целое число N;')

rnd_list = []

import random
def f(name_list, z):
    ''''

    name_list = список имен
    z = к длина созданой последовательности

    Функция создает случайную последоательность из элементов
    в списке name_list, длиой равной к

    '''

    rnd_list = random.choices(name_list, k=z)  # создали рэндомный список длиной k
    print('Готовый список с именами: ', rnd_list) # печатаем созданный лист
    print('Всего имен в списке: ', len(rnd_list))

    #for i in rnd_list:
        #a[i] = a.get(i, 0) + 1 #создал словарь значение=вхождения
    #print('Cписок имен с количеством упоминаний: ', a)
    #print('Самое популярное имя: ', sorted(a, key=a.get, reverse=True)[0]) # определили самое популярное имя
    return rnd_list


f_list = f(sps_list, z = 100)

print()
print('  *  *  ')
print()


# 2. Напишите функцию вывода самого частого имени из списка на выходе функции F;
print('      2. Напишите функцию вывода самого частого имени из списка на выходе функции F; ')



a = {}
def pop_name(list):
    ''''

    Функция pop_name, получает на вход
    список имен и выводит самое популярное

    '''

    for i in list:
        a[i] = a.get(i, 0) + 1   #создал словарь      значение:вхождение
    #print('Cписок имен с количеством упоминаний: ', a)
    very_pop_name = sorted(a, key=a.get, reverse=True)[0]
    #print(very_pop_name)   #ПРО
    return very_pop_name

print(pop_name(f_list))


print()
print('  *  *  *  ')
print()



# 3. Напишите функцию вывода самой редкой буквы, с которого начинаются имена в списке на выходе функции F.
print('       3. Напишите функцию вывода самой редкой буквы, с которого начинаются имена в списке на выходе функции F.')

from collections import Counter

def rare_letter(lst):
    ''''
    Функция rare_letter получает на вход список
    имен и выводит самую редкую букву с которой
    начинается имя

    '''

    y = list(map(lambda x: x[0], lst)) # неотсортированный список из первых букв полученных слов
    #print(y) #  ПРО  Печатаем  неотсортированный список из первых букв  ПРО
    o=Counter(y).most_common()[:-2:-1]  # Нашли самую редковстречающуюся букву в виде словаря
    #print(type(o), o)  # ПРО самую редковстречающуюся букву в виде словаря
    destroy_tuple = (o[0])
    #print(destroy_tuple)  # ПРО выдернули tuple из списка
    jast_letter = destroy_tuple[0]  #Ура  Ура    Ура Я ее выдернул изи tuple
    #print('Самая редкая буква в начале слова: ', jast_letter)
    return jast_letter

print(rare_letter(f_list))





