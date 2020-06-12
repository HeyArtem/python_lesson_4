
# Примеры классов предостовляемые модулем datetime:

from datetime import datetime



print('      Примеры классов предостовляемые модулем datetime:')

d = date(2005, 7,  14)
t = time(12, 30)
s = datetime.combine(d, t)
print('печатаем s:', s)

print('/ /')



print('    datetime.now()')
q=datetime.now()
print('Это время сейчас: ', q)

print('Что за utcnow?')
print(datetime.utcnow())

print()

print('   strptime')
dt = datetime.strptime("21/11/06 16:30", "%d/%m/%y %H:%M")
print('   * * это dt:', dt)


print()


print('timetupl')
tt = dt.timetuple()
print('печатаем tt : ', tt)



print()
print('  **   **   ')
for it in tt:
    print(' печатаем it in tt:', it)

print()
print('    dt.isocalendar  # ISO year # ISO week# ISO weekd')

ic = dt.isocalendar()
for it in ic:
    print('печатаем it in ic: ', it)



print()
print('    dt.strftime("%A, %d. %B %y %I:%M%p")')
print(dt.strftime("%A, %d. %B %y %I:%M%p"))


print()
print('now is', time.strftime("%Y%m%d%h%M%S"))

