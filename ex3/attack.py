import random
from helper import AlgEuclid
def attack():
    #Считывание открытого ключа
    Fin = open ("/mnt/e/crypto/public.txt", "r" )
    temp_string = Fin.read()
    Fin.close
    temp_array = [int(s) for s in temp_string.split() if s.isdigit()]
    N = int(temp_array[1])
    #Разложение чисел на множители методом ρ-эвристики Полларда
    x = 2#random.randint(1,N-2)
    y = 1; i = 0; st = 2
    while AlgEuclid(N,abs(x-y)) == 1:
        if i == st:
            y = x
            st = st * 2
        x =(x*x + 1)%N
        i+=1
    p = AlgEuclid(N,abs(x-y))
    print("p = ",p)
    q = int(N/p)
    print("q = ",q)