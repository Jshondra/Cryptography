def quick(x,d,n):# Алгоритм быстрого возведения в степень
    y = 1
    while d>0:
        if d % 2 == 1:
            y = (y * x) % n
        d = d // 2
        x = (x * x) % n
    return (y)
def AlgEuclid(a,b):#Нахождение НОД(a,b)
    while b != 0:
        t = a % b
        a = b
        b = t
    return(a)
def RAlgEuclid(m,n):#Расширенный алг. Евклида
    a = m; b = n; u1 = 1; v1 = 0; u2 = 0; v2 = 1
    while(b!=0):
        q = a // b
        r = a % b
        a = b; b = r
        r = u2
        u2 = u1 - (q*u2)
        u1 = r
        r = v2
        v2 = v1 - (q*v2)
        v1 = r
    return(u1)

def dec_to_bin(x):
    return int(bin(x)[2:])