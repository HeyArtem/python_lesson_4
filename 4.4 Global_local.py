global_var = 10

def func_exemple(local_var_1, local_var_2):
     print(local_var_1, local_var_2, global_var)
func_exemple(11, 12)

# След пример, мы пытаемся изменить значение перем Global_var в нутри перемен
print('   След пример, мы пытаемся изменить значение перем Global_var в нутри перемен  ')
def func_exemple_1(local_var_1, local_var_2):
    global_var = 20
    print(local_var_1, local_var_2, global_var, id(global_var))
func_exemple_1(11, 12)


# Поменялось ли значение прем global_var??? Проверим
print(' Поменялось ли значение прем global_var??? Проверим')
print(global_var, id(global_var))

# Не поменялось, потому что Global_Var = 10 (ГЛОБАЛЬНАЯ) и Global_var = 20 (ЛОКАЛЬНАЯ) не имеют НИ ЧЕГО ОБЩЕГО
print('!  Не поменялось, потому что Global_Var = 10 (ГЛОБАЛЬНАЯ) и Global_var = 20 (ЛОКАЛЬНАЯ) не имеют НИ ЧЕГО ОБЩЕГО !! ')

print()

#   Служебное слово GLOBAL. Для спец. манипупуляц. с переменными
print('     Служебное слово GLOBAL. Для спец. манипупуляц. с переменными      ')

def func_exemple_1(local_var_1, local_var_2):
    global global_var
    global_var = 20
    print(local_var_1, local_var_2, global_var, id(global_var))

func_exemple_1(11, 12)
print(global_var, id(global_var))

print()

# Так же есть служебное слово    - nonlocal - . C помощью nonlocal можно делать переопределение внутренней области.
print('    Так же есть служебное слово    - nonlocal - . C помощью nonlocal можно делать переопределение внутренней области.  ')

def counter():
    num = 0
    def plus_one():
        nonlocal num
        num+=1
        return num
    return plus_one

count = counter()
print(count)

print('*')
print(count())
# Я не понял!! Что то написали..работает.. а не должно.. еще что то. Более подробный материал будет прикреплен к лекции


print('* * ')
print(count())