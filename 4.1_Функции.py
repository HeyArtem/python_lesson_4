def add(x,y):
    # z=x+y
    # return z  # не пишем эти две строки, заменяем их одной ret x+y
    ''''
Здесь пишем какие передаем параметры.
param x: и его описание
param Y: и его описание
return: что фун-я возвращает

    '''

    return  x+y

help(add)  # так мы можем вызвать описание функции
print(add(100, 101))
print(add('Dima', '+Kate'))



def f1(n):
    def f2(m): # определили новую функцию
        return n+m
    return f2

new_f = f1(100)
print(type(new_f))

new_f = f1(100)
print(new_f(250))

print(' * ')

def f():
    pass
print(f())

# Аргументы функции
print(' Аргументы функции ')
def add(x,y, z = 10): # z не обязательный параметр

    ''''


    '''
    return (x+y+z)
print(add(1, 2))

# или мы указываем z, хотя это не обязательно
print(add(1,2,3))

# Функция с НЕОГРАНИЧЕННЫМ количеством парамеров
print('   ////    Функция с НЕОГРАНИЧЕННЫМ количеством парамеров     \\\\  ')

print('*args она возвра-ет tuple!!')
def function(*args):    # Передает КОРТЕЖ  tuple
    print(type(args), args)
    return args
function(1,2,3, 'Volvo')


print('   ---   **kwargs    создает СЛОВАРЬ  ---')
def function(**kwargs):    # П
    print(type(kwargs), kwargs)
    return kwargs
function(a=1, b=2,c='Volvo', d=1.5)


def func_difficult(x, y=2, *args, **kwargs):
    print(type(kwargs), kwargs)
    return kwargs

func_difficult(1)


print(' - * -')
def func_difficult(x, y=2, *args, **kwargs):
    print(type(x), x)
    print(type(y), y)
    print(type(args), args)
    print(type(kwargs), kwargs)
    return kwargs
func_difficult(1,3, (1,2,3,), temp=12, temp1=13)

func_difficult(1)



