import random
# random() возвращает следующее случайное число с плавающей запятой в промежутке [0.0, 1.0].
print('Вывод случ числа при помощи random.random()')
print(random.random())  # вывели случ число


# Случ число в опред промежутке
print('      Случ число в опредю промежутке   ')

from random import randint
print('Вывод случайного целого числа:', randint(0, 105))
print('Вывод случайного целого числа №2:', randint(0, 105))

print(' * ')

print('  Шаг показывает разницу между каждым числом заданной последовательности. Шаг по умолчанию равен 1, однако его значение можно изменить.')
from random import randrange
print('Вывод случайного целого числа фун-ия randrange: ', randrange(0,10,2)) # 3-е знач=шаг, он же кратность

# Случайный элемент из списка
print('      / / /  Случайный элемент из списка \ \ \  ')

name_list = ['Ваня', 'Зина', 'Артур', 'Илья', 'Семен', 'Просковья', 'Маргарита', 'Альберт', 'Фрэнк', 'Артем', 'Дмитрий']
print('Выбор случ-го имени из списка фун-ия random.choice: ', random.choice(name_list))
print('Выбор случ-го имени из списка фун-ия random.choice попытка 2: ', random.choice(name_list))

print()

# Опред кол-во случайных элем-ов из списка
print('     -    Опред кол-во случайных элем-ов из списка     -  ')
name_list = ['Ваня', 'Зина', 'Артур', 'Илья', 'Семен', 'Просковья', 'Маргарита', 'Альберт', 'Фрэнк', 'Артем', 'Дмитрий']
print('random.sample(): ', random.sample(name_list, 3))
print('random.sample(): ', random.sample(name_list, 3))

print()

# Случайна выборка элемнетов из списка в нужном КОЛИЧЕСТВЕ, позволяет повторять несколько раз один и тот же элемент.
print('   --   Случайна выборка элемнетов из списка в нужном КОЛИЧЕСТВЕ, позволяет повторять несколько раз один и тот же элемент.--  ')
name_list = ['Ваня', 'Зина', 'Артур', 'Илья', 'Семен', 'Просковья', 'Маргарита', 'Альберт', 'Фрэнк', 'Артем', 'Дмитрий']
wtf = random.choices(name_list, k = 100)
print('Выборка методом choices: ', wtf)
print('Проверка, длина wtf равна: ', len(wtf))

print()
print()



# проба домашка
print('    проба домашка   ')
# Создал name_list список с именами
name_list = ['Ваня', 'Зина', 'Артур', 'Илья', 'Семен', 'Просковья','Маргарита', 'Альберт', 'Фрэнк', 'Артем',
             'Дмитрий', 'София', 'Ева', 'Ромео', 'Джульетта', 'Фокс', 'Карбофос', 'Фунтик', 'Том', 'Джери']
print('Всего слов в name_list: ',len(name_list))

print()

def rnd_name(name_list, z):
    rnd_list = random.choices(name_list, k=z)
    print(rnd_list)
    print('Всего имен в списке: ', len(rnd_list))
    return rnd_list

rnd_name(['Ваня', 'Зина', 'Артур', 'Илья', 'Семен', 'Просковья','Маргарита', 'Альберт', 'Фрэнк', 'Артем',
             'Дмитрий', 'София', 'Ева', 'Ромео', 'Джульетта', 'Фокс', 'Карбофос', 'Фунтик', 'Том', 'Джери'], z=100)



# 2. Напишите функцию вывода самого частого имени из списка на выходе функции F;
name_list = ['Ваня', 'Зина', 'Артур', 'Илья', 'Семен', 'Джульетта', 'Просковья','Маргарита', 'Альберт', 'Просковья','Фрэнк', 'Артем',
             'Дмитрий', 'София', 'Ева', 'Ваня', 'Ромео', 'Ваня', 'Джульетта', 'Фокс', 'Карбофос', 'Фунтик', 'Том', 'Джери']


# pop_words = []
# def popWords(name_list):


name_list = ['Ваня', 'Зина', 'Артур', 'Илья', 'Зина', 'Семен', 'Джульетта', 'Просковья', 'Зина', 'Маргарита', 'Альберт', 'Просковья','Фрэнк', 'Артем',
             'Дмитрий', 'София', 'Ева', 'Ваня', 'Ромео', 'Ваня', 'Джульетта', 'Фокс', 'Карбофос', 'Фунтик', 'Том', 'Джери']



# 2. Напишите функцию вывода самого частого имени из списка на выходе функции F;
print('  ///    2. Напишите функцию вывода самого частого имени из списка на выходе функции F; \\\    ')

#name_listRnd = ['Ваня', 'Зина', 'Артур', 'Илья', 'Зина', 'Семен', 'Джульетта', 'Просковья', 'Зина', 'Маргарита', 'Альберт', 'Просковья','Фрэнк', 'Артем',
#             'Дмитрий', 'София', 'Ева', 'Ваня', 'Ромео', 'Ваня', 'Джульетта', 'Фокс', 'Карбофос', 'Фунтик', 'Том', 'Джери']

a = {}
asd = {}

import random
def rnd_name(name_listRnd, z):
    ''''

    name_list = список имен
    z = к длина созданой последовательности

    Функция создает случайную последоательность из элементов
    в списке name_list, длиой равной к

    '''

    rnd_list = random.choices(name_list, k=z)
    print(rnd_list)
    print('Всего имен в списке: ', len(rnd_list))

    for i in rnd_list:
        a[i] = a.get(i, 0) + int(1)


    print('Cписок имен с количеством упоминаний: ', a)
    print('Самое популярное имя: ', sorted(a, key=a.get, reverse=True)[0])

    return rnd_list


rnd_name(['Ваня', 'Зина', 'Артур', 'Илья', 'Семен', 'Джульетта', 'Просковья','Маргарита', 'Альберт', 'Просковья','Фрэнк', 'Артем',
             'Дмитрий', 'София', 'Ева', 'Ваня', 'Ромео', 'Ваня', 'Джульетта', 'Фокс', 'Карбофос', 'Фунтик', 'Том', 'Джери'], z=100)

print(asd)

print('*  *  *  *  *  *')
# z = 10
# biba_list = ['Карлсон', 'Дюймовочка', 'Михайло', 'Буратино']
# new_f = rnd_name(biba_list, z)



# a = {}
# for i in name_list2:
#     a[i] = a.get(i, 0) + int(1)
# print('Отсортированный список имен с количеством упоминаний: ', a)
# print('Самое популярное имя: ', sorted(a, key=a.get, reverse=True)[0])

def f(lst):
    elems = {}
    e, em = None, 0
    for i in lst:
        elems[i] = t = elems.get(i, 0) + 1
        if t > em:
            e, em = i, t
    return e

print(f(['a', 'abc', 'def', 'b', 'abc', 'c']))


# def rare_letter(list_names_random):
#     first_letter_list = []
#     first_letter = ''
#
#     for name in list_names_random:
#         first_letter = name[0]
#         first_letter_list.append(first_letter)
#
#     print(first_letter_list, len(first_letter_list))
#     dict_rare_letter = {a: first_letter_list.count(a) for a in first_letter_list}
#     print(dict_rare_letter)
#
#     letter_values = []
#     for values in dict_rare_letter.values():
#         letter_values.append(values)
#     rare_letter_list  = []
#     for items, values in dict_rare_letter.items():
#         if values == min(letter_values):
#             rare_letter_list.append(items)
#     print(rare_letter_list)
#     return rare_letter_list
#
#
# rare_letter(list(['Ваня', 'Зина', 'Артур', 'Илья', 'Семен', 'Джульетта', 'Просковья','Маргарита', 'Альберт', 'Просковья','Фрэнк', 'Артем',
#              'Дмитрий', 'София', 'Ева', 'Том', 'Джери']))



print(' \    \    \    map полигон')

y=20
def mult(x): # Фу-я умножае и распечат результат, активируется вызовом имени
    r = x * 2
    print(r)
    return r
mult(y) # Активация mult(x)











