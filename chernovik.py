import random

# random() возвращает следующее случайное число с плавающей запятой в промежутке [0.0, 1.0].
print('Вывод случ числа при помощи random.random()')
print(random.random())  # вывели случ число

# Случ число в опред промежутке
print('      Случ число в опредю промежутке   ')

from random import randint
print('Вывод случайного целого числа:', randint(0, 105))
print('Вывод случайного целого числа №2 :', randint(0, 105))

print(' * ')
print('  Шаг показывает разницу между каждым числом заданной последовательности. Шаг по умолчанию равен 1, однако его значение можно изменить.')
from random import randrange
print('Вывод случайного целого числа', randrange(0,10,2)) # 3-е знач=шаг, он же кратность

# Случайный элемент из списка
print('      / / /  Случайный элемент из списка \ \ \  ')

name_list = ['Ваня', 'Зина', 'Артур', 'Илья', 'Семен', 'Просковья', 'Маргарита', 'Альберт', 'Фрэнк', 'Артем', 'Дмитрий']
print('Выбор случ-го имени из списка: ', random.choice(name_list))

# НЕсколько случайных элем-ов из списка
print('     -    НЕсколько случайных элем-ов из списка     -  ')
name_list = ['Ваня', 'Зина', 'Артур', 'Илья', 'Семен', 'Просковья', 'Маргарита', 'Альберт', 'Фрэнк', 'Артем', 'Дмитрий']
print('random.sample(): ', random.sample(name_list, 3))

print()

# Случайна выборка элемнетов из списка в нужном КОЛИЧЕСТВЕ, позволяет повторять несколько раз один и тот же элемент.
print('   --   Случайна выборка элемнетов из списка в нужном КОЛИЧЕСТВЕ, позволяет повторять несколько раз один и тот же элемент.--  ')
name_list = ['Ваня', 'Зина', 'Артур', 'Илья', 'Семен', 'Просковья', 'Маргарита', 'Альберт', 'Фрэнк', 'Артем', 'Дмитрий']
wtf = random.choices(name_list, k = 100)
print('Выборка методом choices: ', wtf)

print()
print()




# проба домашка
print('    проба домашка   ')

name_list = ['Ваня', 'Зина', 'Артур', 'Илья', 'Семен', 'Просковья','Маргарита', 'Альберт', 'Фрэнк', 'Артем',
             'Дмитрий', 'София', 'Ева', 'Ромео', 'Джульетта', 'Фокс', 'Карбофос', 'Фунтик', 'Том', 'Джери']
print('Всего слов в name_list: ',len(name_list))




# import random
#
# def nameRnd():
#     k = 10
#     name_list = ['Ваня', 'Зина', 'Артур', 'Илья']
#     print(random.choices(name_list, k = 25))
#
#
#
# nameRnd()





# import random
#
# def nameRnd():
#     k = 10
#     name_list = ['Ваня', 'Зина', 'Артур', 'Илья']
#     print(random.choices(name_list, k = 10))
nameRnd()



# def nameRnd_2(name_list, k):
#     random_result = (random.choices(name_list, k))
#     print(random_result)
#     return random_result
#
# nameRnd_2(name_list = ['Ваня', 'Зина', 'Артур', 'Илья'], k = 2)
# nameRnd_2()
#print(nameRnd_2())






# def sos():
#     a = int(input())
#     b = int(input())
#     print(('Всего ', a+b, ' шт.'))
# print('Сколько бананов и ананасов для обезьян ?')
# sos()




#print(total)


#nameRnd(list1 = ['Ваня', 'Зина', 'Артур', 'Илья'], k = 100)



# def random_name(name_list, k = 100):
#
#     """
#     name_list = список имен
#     к= длина созданой последовательности
#
#     Функция создает случайную последоательность из элементов
#     в списке name_list, длиой равной к
#
#
#     """
#     wtf2 = random.choices(name_list, k)
#     print(wtf2)
#     return wtf2
#
# random_name(name_list = ['Ваня', 'Зина', 'Артур', 'Илья', 'Семен', 'Просковья', 'Маргарита', 'Альберт', 'Фрэнк', 'Артем',
#              'Дмитрий', 'София', 'Ева', 'Ромео', 'Джульетта', 'Фокс', 'Карбофос', 'Фунтик', 'Том', 'Джери'], k=100)
# print(random_name())

print('- * - * -* -')



# print(random_name('Ваня', 'Зина', 'Артур', k = 100))


# name_list = ['Ваня', 'Зина', 'Артур', 'Илья', 'Семен', 'Просковья','Маргарита', 'Альберт', 'Фрэнк', 'Артем',
#              'Дмитрий', 'София', 'Ева', 'Ромео', 'Джульетта', 'Фокс', 'Карбофос', 'Фунтик', 'Том', 'Джери']
# print(random_name(name_list))