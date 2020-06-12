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


print()
print('  -    -    ')
print()

#  4. В файле с логами найти дату самого позднего лога (по метке времени):
print('      4. В файле с логами найти дату самого позднего лога (по метке времени): ')
print()






with open('log', 'r') as f:
    from datetime import datetime
    lines = f.readlines()  # Сделали список из лога
    print('печатаю перемен lines: ', lines) #ПРО
    all_date_times = list(map(lambda i: i.split(',')[0], lines)) # напечатали только дату
    print('печатаю all_date_times: ', all_date_times)
    all_date_times.sort(key=lambda date: datetime.strptime(date, '%Y-%m-%d %H:%M:%S')) # отсортирована дата от ранней к последней
    print('All date times which are sorted Даты отсортированы:\n', all_date_times)
    print('The latest log line is: ', all_date_times[len(all_date_times)-1])






print(' - * - * - ')
print(' - * - * - ')

f = open(r"C:\Users\artem\Documents\Артем\PycharmProjects\python_lesson_4\log", "r")
text = f.read()
print(text)
print(type(text))
f.close()



# from datetime import datetime

take_date =list(map(lambda i: i.split(' ')[0], text)) #перебираем каждого участника, тут неважно что будет стоять в качестве разделителя
# не понимаю для чего [0], возможно это на сколько часте разбивать. Вывод првратили строку в список состоящий из каждого элемента
print(take_date)
print('тип перемен take_date: ', type(take_date))

print('Хочу методом replace заменить "\\n" на " " : ')
split_noN = text.replace("\n", " ")
print('шаг 1 удалили заменили переносы строки на " , ": ', split_noN)
print(type(split_noN))


s=' '.join(take_date) # склеили по точке
print(s)

print('Хочу методом replace заменить " " на " " : ')
split_noN_br = text.replace(" ", "")
print('шаг 1 удалили заменили переносы строки на " , ": ', split_noN_br)
print(type(split_noN_br))

#take_date.sort(key=lambda date: datetime.strptime(date, '%y-%m-%d %H:%M:%S'), reverse=True)   # ТАК И НЕ ЗАРАБОТАЛО ПОЧЕМУ???

# ГОВНО!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!


# sort -сортирет по возрастанию или убыванию (sorted-СОЗДАЕТ НОВУЮ отсор-ю после-ть), если указать «reverse = true»,
# список будет отсортирован в порядке убывания. ВИД  -> sort[List_name.sort(key = …, reverse = ...)]
# key -ключ по которому сортируем, в данном случае это функция(lambda)
# здесь lambda - datetime.strptime - преобразует строку в datetime
#print(take_date2)
# all_date_times.sort(key=lambda date: datetime.strptime(date, '%Y-%m-%d %H:%M:%S'), reverse=True)


#print()

print('Хочу методом replace заменить \\n на "." : ')
split_noN = text.replace("\n", ". ")
print('шаг 1 удалили заменили переносы строки на " , ": ', split_noN)
print(type(split_noN))







print()

print()
print('        сортирую по запятой  , ')

split1 = text.split(",")
print(type(split1))
print("split1 :",  split1)



print()

# # делаю из split1 строку, т.к. split не хочет работать с List странно вооюще
# print('делаю из split1 строку, т.к. split не хочет работать с List странно вооюще')
# sp1 = str(split1)

print()
# print('сортирую по запятой')  # Это добавляет [" [блаБла]"]  только усложняет
# sp2=sp1.split(",")
# print('это sp2после сортировки по запятым', sp2)
# print(type(sp2))




# split2 = sp1.split(",") # разделил по запятой
# print(type(split2))
# print(split2)

print()

print('!!! !!!')
# NEW Метод  -  replace      -> str.replace(old, new, count)<- можно без count
print('      NEW Метод  -  replace      -> str.replace(old, new, count)<- можно без count')
print('Hello'.replace('l', '-Ж-'))

print()

po = ('Зина, Артур, Илья, Семен, Просковья,Маргарита, Альберт')
po1 = po.replace('а', ' - БАЦ - ')
print('В перемен-ой заменили a на БАЦ: работает, но весь текст должен быть в кавычках', po1)






print()
# print('печатаю первый и третий элемент')
# print(split[0]) # печатаем конкретный элемент
# print(split[2])






print(' - * - ')

# sps_list = text.split('\n')
# print(type(sps_list), sps_list)

# strX = str(sps_list) # пробую перевести в строку
# print(type(strX), strX)
#

print(' - * * - ')


# split2 = strX.split(",") # разделил по запятой
# print(type(split2))
# print(split2)












# lines = f.readlines()
# print(lines)
# all_date_times = list(map(lambda i: i.split(',')[0], lines))
# print(all_date_times)
# all_date_times.sort(key=lambda date: datetime.strptime(date, '%y-%m-%d %H-%M-%S'), reverse=True)
# print('All date times which are sorted:\n', all_date_times)
# print('The latest log line is: ', all_date_times[len(all_date_times)-1])
















