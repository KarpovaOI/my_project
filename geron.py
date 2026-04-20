import math


def geron(a, b, c):
    p = (a+b+c)/2
    r = ''
    if a < 0 or b < 0 or c < 0:
        r = 'длина не может быть отрицательной'
    else:
        r = round(math.sqrt(p*(p-a)*(p-b)*(p-c)), 3)
    return (r)


r1 = float(input('Введите длину a: '))
r2 = float(input('Введите длину b: '))
r3 = float(input('Введите длину c: '))

print('Решение: ', geron(r1, r2, r3))
