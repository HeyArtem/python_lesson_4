sps_list = (['Ваня', 'Зина', 'Артур', 'Илья', 'Семен', 'Джульетта', 'Просковья','Маргарита', 'Альберт', 'Просковья','Фрэнк', 'Артем',
             'Дмитрий', 'София', 'Ева', 'Ваня', 'Ромео', 'Ваня', 'Джульетта', 'Фокс', 'Карбофос', 'Фунтик', 'Том', 'Джери'])

a = {}
import random
def f(name_list, z):
    ''''

    name_list = список имен
    z = к длина созданой последовательности

    Функция создает случайную последоательность из элементов
    в списке name_list, длиой равной к

    '''

    rnd_list = random.choices(name_list, k=z)  # создали рэндомный список длиной k
    print(rnd_list) # печатаем созданный лист
    print('Всего имен в списке: ', len(rnd_list))
    for i in rnd_list:
        a[i] = a.get(i, 0) + 1 #создал словарь значение=вхождения
    print('Cписок имен с количеством упоминаний: ', a)
    print('Самое популярное имя: ', sorted(a, key=a.get, reverse=True)[0]) # определили самое популярное имя
    return rnd_list

#f(sps_list, z = 100)
f_list = f(sps_list, z = 100)

print('  *  *  *  *  ')
print('результат после определения частог имени')
print(type(f_list), f_list)

print()
print('       *   *  3.переходим к 3 части, поиску редкой первой буквы    *    *')


from collections import Counter

def rare_letter(lst):
    y = list(map(lambda x: x[0], lst)) # неотсортированный список из первых букв
    print(y) #  ПРО  Печатаем  неотсортированный список из первых букв  ПРО
    o=Counter(y).most_common()[:-2:-1]  # Нашли самую редковстречающуюся букву в виде словаря
    print(type(o), o)  # ПРО самую редковстречающуюся букву в виде словаря
    destroy_tuple = (o[0])
    print(destroy_tuple)  # ПРО выдернули tuple из списка
    jast_letter = destroy_tuple[0]  #Ура  Ура    Ура Я ее выдернул изи tuple
    print('Самая редкая буква в начале слова: ', jast_letter)
    return jast_letter
print(rare_letter(f_list))



#o=Counter('yyyyuuuuewwffffdedekjkjkjfrfrfiruiuiugtgtgtcfffttt').most_common()[:-2:-1]
#print(o) #!!! Я не знаю почему -2, это я эксперементальнообнаружил



#from collections import Counter

list_f = (['Ваня', 'Зина', 'Артур', 'Илья', 'Семен', 'Джульетта', 'Просковья','Маргарита', 'Альберт', 'Просковья','Фрэнк', 'Артем',
             'Дмитрий', 'София', 'Ева', 'Ваня', 'Ромео', 'Ваня', 'Джульетта', 'Фокс', 'Карбофос', 'Фунтик', 'Том', 'Джери'])

#y = []
# def rare_letter(lst):
#     # lst = map(lambda x: x[0], lst) #Список из первых букв?
#     # return Counter(lst).most_common()[-1:][0][0]
#     y = list(map(lambda x: x[0], lst))
#     #print(y) #Печатаем  неотсортированный список из первых букв
#     return y
#
# print(rare_letter(list_f))



print()
print()

# Сортировка по ПЕРВОЙ БУКВЕ                                  !!!НЕ ЗАКОНЧЕНО!!!!
print('     Сортировка по ПЕРВОЙ БУКВЕ    ')

list_f2 = (['Ваня', 'Зина', 'Артур', 'Илья', 'Семен', 'Джульетта', 'Просковья','Маргарита', 'Альберт', 'Просковья','Фрэнк', 'Артем',
             'Дмитрий', 'София', 'Ева', 'Ваня', 'Ромео', 'Ваня', 'Джульетта', 'Фокс', 'Карбофос', 'Фунтик', 'Том', 'Джери'])

list_name_sort_key = sorted(list_f2, key=lambda x: x[0])
print(list_name_sort_key)

print('Знакомство с Counter')
print('Знакомство с Counter')

# Знакомство с Counter
print('   Знакомство с Counter  ')
# collections.Counter - вид словаря, который позволяет нам считать количество
# неизменяемых объектов (в большинстве случаев, строк).

import collections

b = collections.Counter()  # Создадим словарь:  ИМЯ:ЧИСЛО (кол-во вхождений)
for i in ['spam', 'Дятел', 'egg', 'Дятел', 'spam', 'Дятел', 'counter', 'counter', 'Дятел', 'counter', 'Дятел']:
    b[i] += 1
print(b)

print(b['Дятел']) # Вывод сколько раз встречается конкретное слово

print(b['spam'])
print(b['collections'])


# Counter с листами
print('# Counter с листами')

from collections import Counter

lst1 = [5,6,7,1,3,9,9,1,2,5,5,7,7]
c = Counter(lst1)
print(c)





print()

# elements() - возвращает список элементов в лексикографическом порядке.
print('   elements() - возвращает список элементов в лексикографическом порядке.  ')


from collections import Counter   # напечататет каждую букву указанное количество раз
c = Counter(a=4, b=2, c=0, d=-2)
print(list(c.elements()))

print()
print()

# most_common([n]) - возвращает n наиболее часто встречающихся элементов,
# в порядке убывания встречаемости. Если n не указано, возвращаются все элементы.
print('   most_common([n]) - возвращает n наиболее часто встречающихся элементов,   ')

d=Counter('abracadabra').most_common()
print('most_common(): ',d)

a=len('abracadabra')
print(a)
d = Counter('abracadabra').most_common(1) # вернет только самый популярный символ
print(d)





# c.most_common()[:-n:-1] - n наименее часто встречающихся элементов. Кто бы мог подумать
print(' c.most_common()[:-n:-1] - n наименее часто встречающихся элементов. Кто бы мог подумать ')
from collections import Counter

e=Counter('abracadabra').most_common()[:-3:-1] # [:-n:-1] - n наименее часто встречающихся элементов.
print(e)

p=Counter('ewwtttyyyyuuuufffffff').most_common()[:-2:-1]
print(p)

o=Counter('yyyyuuuuewwffffdedekjkjkjfrfrfiruiuiugtgtgtcfffttt').most_common()[:-2:-1]
print(o) #!!! Я не знаю почему -2, это я эксперементальнообнаружил


print('/    /    /    /    /    /    /    ')

# subtract([iterable-or-mapping]) - вычитание
print('        subtract([iterable-or-mapping]) - вычитание  ')

c = Counter(a =4, b=2, c=0, d=-2) # a из скобки 'd', вучтут из 'a' из скобки 'c'
d = Counter(a =1, b=2, c=3, d=-4) # у меня опять не работает
(c.subtract(d)) # такой должен быть ответ: Counter({'a': 3, 'b': 0, 'c': -3, 'd': -6})






print()
print()
# С предложением
print('      С предложением       С предложением')

s = 'the lazy dog jumped over another lazy dog'
words = s.split()
uy = Counter(words)  # просто расхерачиваю предложение по словам и в словарь его
print(uy)







print(' * * *  * * * *  ** * * * * ')
print(' удалить элементы, встречающиеся менее одного раза.     ')

from collections import Counter
# rt=('yyyyuuuuewwffffdedekjkjkjfrfrfiruiuiugtgtgtcfffttt') += Counter(1)
#print(rt)




#print('  **  **  ** ')



# Словарь    Словарь     Словарь    Словарь     Словарь    Словарь     Словарь    Словарь
print('  Словарь    Словарь     Словарь    Словарь     Словарь    Словарь     Словарь    Словарь     ')

# print('словарь, отсортированный по ключу   словарь, отсортированный по ключу')
# print(' - orderedDict(sorted(d.items(), key=lambda t: t[0])) - ')
#
#
# zizi_dict = {'banana': 3, 'apple': 4, 'pear': 1, 'orange': 2}
#
# qw = zizi_dict(sorted(d.items(), key=lambda t: t[0]))
# print(qw)
#
# wq = zizi_dict(sorted(d.items(), key=lambda t:t[1]))
# print(wq)