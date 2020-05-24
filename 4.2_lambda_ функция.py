def ident(x):
    return x
print(ident(10))

# Альтернатива в стиле lambda

print((lambda x: x)(10))
print((' * '))
ident_lambda = lambda x: x
print(ident_lambda(10))


print('  *  *  ')
# увидь! title  меняет регистр первой буквы
print(' увидь! title  меняет регистр первой буквы !!!')
car = lambda brend, engin_volume, price: f'Car: {brend.title()}, Engine volume: {engin_volume}, Price: {price}'
print(car('volvo', 1.5, 13000000))

# ТИп тип
print('  ТИп тип !!!!! Какой тип?')
print(type(ident), type(ident_lambda))