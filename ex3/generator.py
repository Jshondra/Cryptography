import random
from helper import quick
from helper import AlgEuclid
from helper import RAlgEuclid
from helper import dec_to_bin

def gen_prime(L):
    p = random.randint(1, 2**int((L/2)))
    q = random.randint(1, 2**int((L/2)))
    #Проверка простых чисел
    i=0
    while i < 10:
        a = random.randint(1, p-1)
        if quick(a,p-1,p) == 1:
            i=i+1
        else:
            i=0
            p = random.randint(1, 2**int((L/2)))
            continue
    i=0
    while i < 10:
        a = random.randint(1, q-1)
        if quick(a,q-1,q) == 1:
            i=i+1
        else:
            i=0
            q = random.randint(1, 2**int((L/2)))
            continue
    N = p * q
    print("N = ",N)
    F = (p-1)*(q-1)
    #Создание открытой экспоненты
    e = random.choice([3,17,257,65537])
    while AlgEuclid(e,F) != 1 or e >= N:
        e = random.choice([3,17,257,65537])
    print("e = ",e)
    #Создание закрытой экспоненты
    d = RAlgEuclid(e,F)
    if d < 0:
        d = d + F
    print("d = ",d)
    #Запись в файл
    Fout = open ( "/mnt/e/crypto/public.txt", "w" )
    Fout.write("{:d} {:d}".format(e,N))
    Fout.close()
    Fout = open ( "/mnt/e/crypto/private.txt", "w" )
    Fout.write("{:d} {:d}".format(d,N))
    Fout.close()
def gen_not_prime(L):
    p = random.randint(1, 2**int((L/2)))
    q = random.randint(1, 2**int((L/2)))
    #Проверка составных чисел
    a = random.randint(1, p-1)
    while quick(a,p-1,p) == 1:
        p = random.randint(1, 2**int((L/2))) 
    a = random.randint(1, q-1)
    while quick(a,q-1,q) == 1:
        q = random.randint(1, 2**int((L/2)))
    #Вывод данных
    N = p * q
    F = (p-1)*(q-1)
    #Создание открытой экспоненты
    e = random.choice([3,17,257,65537])
    while AlgEuclid(e,F) != 1 or e >= N:
        e = random.choice([3,17,257,65537])
    print("e = ",e)
    #Создание закрытой экспоненты
    d = RAlgEuclid(e,F)
    if d < 0:
        d = d + F
    print("d = ",d)
    #Запись в файл
    Fout = open ( "/mnt/e/crypto/public.txt", "w" )
    Fout.write("{:d} {:d}".format(e,N))
    Fout.close()
    Fout = open ( "/mnt/e/crypto/private.txt", "w" )
    Fout.write("{:d} {:d}".format(d,N))
    Fout.close()
def gen_prime_test(L,r):
    p = random.randint(1, 2**int(L*r))
    q = random.randint(1, 2**int(L*(1-r)))
    #Проверка простых чисел
    i=0
    while i < 10:
        a = random.randint(1, p-1)
        if quick(a,p-1,p) == 1:
            i=i+1
        else:
            i=0
            p = random.randint(1, 2**int(L*r))
            continue
    i=0
    while i < 10:
        a = random.randint(1, q-1)
        if quick(a,q-1,q) == 1:
            i=i+1
        else:
            i=0
            q = random.randint(1, 2**int(L*(1-r)))
            continue

    #Вывод данных
    N = p * q
    F = (p-1)*(q-1)
    #Создание открытой экспоненты
    e = random.choice([3,17,257,65537])
    while AlgEuclid(e,F) != 1 or e >= N:
        e = random.choice([3,17,257,65537])
    #Создание закрытой экспоненты
    d = RAlgEuclid(e,F)
    if d < 0:
        d = d + F
    #Запись в файл
    Fout = open ( "/mnt/e/crypto/public.txt", "w" )
    Fout.write("{:d} {:d}".format(e,N))
    Fout.close()
    Fout = open ( "/mnt/e/crypto/private.txt", "w" )
    Fout.write("{:d} {:d}".format(d,N))
    Fout.close()
