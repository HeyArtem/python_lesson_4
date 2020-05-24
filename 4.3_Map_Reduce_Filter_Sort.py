# map
# Определим функцию, которая будет переводить МИли в километры
print('map    Определим функцию, которая будет переводить МИли в километры')

def miles_to_km(miles):
    return miles * 1.6
mile_dist = [1.0, 1.6, 2.3]

km_dist = list(map(miles_to_km, mile_dist)) # list  потому что map возвр-ет свой спецефич. тип
print((type(km_dist), km_dist))
# Тоже, но с лямбда
print(' Тоже, но с лямбда ')

km_dist = list(map(lambda x: 1.6*x, mile_dist))
print((type(km_dist), km_dist))

# функция MAP  может работать с несколькими списками
print(' функция MAP  может работать с несколькими списками ')
list1 = [1, 2, 3]
list2 = [4, 5, 6]
list3 = list(map(lambda x,y: x*y, list1, list2))
print(type(list3), list3)

# Функ-я reduce. Её нужно вызывать начиная с 3 версии
print(' Функ-я reduce. Её нужно вызывать начиная с 3 версии ')
print(' Найдем max. значение')

from functools import reduce
list_temp = [43, 12, 41, 100, 101, 4]
max = reduce(lambda a, b: a if a>b else b, list_temp)
print(type(max), max)

print()
# Функция filter
print('         Функция filter    ')
print('  Найдем элементы которые > 50')
# Функ-ия filter на выходе имеет свой тип, поэтому будем приводить ее к list

print('  Функ-ия filter на выходе имеет свой тип, поэтому будем приводить ее к list ')

list_temp = [43, 12, 41, 100, 101, 4]
list50 = list(filter(lambda x: x>50, list_temp))
print(list50)

print(' * ')
list_temp = [43, 12, 41, 100, 101, 4]
list50 = list(filter(lambda x: x%10==1, list_temp))
print(list50)


print()


# Функция sorted. Принимает list и возвращает list
print('         Функция sorted. Принимает list и возвращает list  ')

list_temp = [43, 12, 41, 100, 101, 4]
list_temp_sort = sorted(list_temp)
print(list_temp_sort)


print('   Сортировка в обратном порядке  ')

list_temp = [43, 12, 41, 100, 101, 4]
list_temp_sort_revers = sorted(list_temp, reverse=True)
print(list_temp_sort_revers)

print(' *  *  *')
# Сортировка строк
print('    Сортировка строк  ')

list_names = ['Kate', 'Dima', 'Ivan', 'Make'] # В алфавмитном порядке
list_name_sort = sorted(list_names)
print(list_name_sort)

# Сортировка по ВТОРОЙ БУКВЕ
print('     Сортировка по ВТОРОЙ БУКВЕ    ')
list_names = ['Kate', 'Dima', 'Ivan', 'Make']
list_name_sort_key = sorted(list_names, key=lambda x: x[1])
print(list_name_sort_key)