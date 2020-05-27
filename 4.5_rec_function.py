# Рекурсивные функции
print('                          Рекурсивные функции                 ')

print('factorial методом пекурсивной функции')

def fact(num):
    if num == 0:
        return 1
    else:
        return num * fact(num - 1)
print(fact(10))

print()

# То же самое, но В ЦИКЛЕ
print('        То же самое, но В ЦИКЛЕ         ')

factorial = 1
for i in range(1, 11):
    factorial *= i
print(factorial)

# Возведение в степень (a*b) с помощью Рекурсивной ф-ции
print('         Возведение в степень (a*b) с помощью Рекурсивной ф-ции ')
def degree(a,b):
    if b == 0:
        return 1
    else:
        return a * degree(a,b-1)
print(degree(2, 10))

print()

# То же самое (возведение в степень), но В ЦИКЛЕ
print('         То же самое(возведение в степень), но В ЦИКЛЕ         ')
deg = 1
for i in range(1, 11):
    deg *= 2
print(deg)
# Рекурсию редко используют, она может занять всю оперативную память, но иногда попадаются очень красивые решения,
# котор. использ-ют Рекур-ую функцию

print('! !   Рекурсию редко используют, она может занять всю оперативную память,! !')