import math
a = -3
b = 8
c = 11
d = b**2-4*a*c
r = ''
if d < 0:
    r = 'действительных корней нет'
else:
    x1 = (-b-math.sqrt(d))/(2*a)
    x2 = (-b+math.sqrt(d))/(2*a)
    r = 'x1='+str(round(x1, 3))+'\nx2='+str(round(x2, 3))
print(r)
