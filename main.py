import math


def qvadra(a, b, c):
    d = b**2-4*a*c
    r = ''
    if d < 0:
        r = 'действительных корней нет'
    else:
        x1 = (-b-math.sqrt(d))/(2*a)
        x2 = (-b+math.sqrt(d))/(2*a)
        r = '\nx1='+str(round(x1, 3))+'\nx2='+str(round(x2, 3))
    return (r)


r1 = float(input('Введите a: '))
r2 = float(input('Введите b: '))
r3 = float(input('Введите c: '))

print('Решение: ', qvadra(r1, r2, r3))
