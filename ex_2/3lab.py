import math
import random

def createbi(k):

    r=random.randint(0,pow(2,k)-1)
    r=bin(r)[2:]
    if (len(r)!=k):
        num=k-len(r)
        zeros='0'*num
        r=zeros+r
    with open('random_binary.txt', mode='w') as file:
        file.write(r)
    return r

def lfsr(taps,n):

    k = int(taps[0])
    createbi(k)
    with open('random_binary.txt') as f:
        seed = f.read()

    sr, xor = seed, 0
    m=[]
    for i in range(n):
        m.append(sr[len(sr) - 1])
        for t in taps:
            xor ^= int(sr[len(sr)-t])
        sr= str(xor) + sr[:-1]
        xor=0
    # if sr == seed:

    # break
    m_str = ''.join(m)
    with open('m-ansamble.txt','w') as mfile:
        mfile.write(m_str)
    return m_str

def moment(k,m):

    sum=0
    N=len(m)
    for j in range (1,N-k):
        sum+=int(m[j])
    sum=sum/(N-1-k)

    return sum

def momentk(k,m):
    N=len(m)
    sum=0
    for j in range (k+1,N):
        sum+=int(m[j])
    sum=sum/(N-k-1)
    return sum

def cov(k,m):
    N=len(m)
    count=1
    sum=0
    mo=moment(k, m)
    mok=momentk(k,m)
    for i,j in zip(range(1,N-k),range(k+1,N)):
        sum+=(int(m[i])-mo)*(int(m[j])-mok)
        count+=1
    sum=sum/count

    return sum

def disp(k,m):
    return moment(k,m)-moment(k,m)**2

def dispk(k,m):
    return momentk(k,m)-momentk(k,m)**2

def corrtest(m,k):
    N=len(m)
    R=0
    R=cov(k,m)/math.sqrt(disp(k,m)*dispk(k,m))
    print("R=",R)
    ocenka=1/(N-1)+2/(N-2)*math.sqrt(N*(N-3)/(N+1))
    print("оценка",ocenka)
    print("выполнилось?",math.fabs(R)<ocenka)
    
def serialtest(m,kol):
    N = len(m) / kol
    group=([m[i:i+int(kol)] for i in range(0, len(m),int(kol))])
    # print("сгруппированная последовательность",group)
    d=dict()
    for i in group:
        d[i]=group.count(i)
    Nt=N/pow(2.0,kol)
    print("теоритическое Nt=",Nt)
    l=[]
    print(d)
    for key, value in d.items():
        l.append(value)
    while len(l)<pow(2,kol):
        l.append(0)
    print("экспериментальные Nэ=",l)
    sum=0.0
    for i in l:
        sum+=pow((i-Nt),2.0)/Nt
    print("хи^2 =",sum)

def encrypt():
    print("Шифрование")
    f = open('file.txt', 'rb')
    d = f.read()
    f.close()
    res=""
    for i in range(len(d)):
        res+=bin(d[i])[2:]
    with open('m-ansamble.txt') as f:
        key= f.read()
    print("Ключ",key)
    print("Открытый текст",res)
    encrypt=""
    for i,k in zip((res),(key)):
        tmp=int(i)^int(k)
        encrypt+=str(tmp)
    print("Зашифрованный текст",encrypt)
    with open('encrypt.txt', mode='w') as enc:
        enc.write(encrypt)
    print("результат записан в 'encrypt.txt'")

def decrypt():

    print("Дешифрование")
    with open('m-ansamble.txt', mode='r') as k:
        key=k.read()
    f = open('encrypt.txt', 'r')
    enc = f.read()
    f.close()
    print("Ключ",key)
    print("Зашифрованный текст",enc)
    encrypt=""
    for i,k in zip((enc),(key)):
        tmp=int(i)^int(k)
        encrypt+=str(tmp)
    print("Открытый текст",encrypt)
    print(len(encrypt))
    with open('decrypt.txt', mode='w') as enc:
        enc.write(encrypt)
    print("результат записан в 'decrypt.txt'")
print("Введите число степеней полинома:")
chislo = int(input())
pol = []
print("Введите степени полинома:")
for i in range(chislo):
    stepen = int(input())
    pol.append(stepen)
k = int(pol[0])
razr = k
print(pol)
m=lfsr(pol,15000)
print("длина серии")
slen=int(input())
serialtest(m,slen)
print()
print("k=1 для корреляционного теста Rk")
corrtest(m,1)
print("k=2 для корреляционного теста Rk")
corrtest(m,2)
print("k=3 для корреляционного теста Rk")
corrtest(m,3)
print("k=4 для корреляционного теста Rk")
corrtest(m,4)
print("k=5 для корреляционного теста Rk")
corrtest(m,5)
print("k=6 для корреляционного теста Rk")
corrtest(m,6)
print("k=7 для корреляционного теста Rk")
corrtest(m,7)
print("k=8 для корреляционного теста Rk")
corrtest(m,8)
print("k= 9для корреляционного теста Rk")
corrtest(m,9)

encrypt()
print()
decrypt()
e = open('encrypt.txt', 'r')
enc = e.read()
e.close()
print("Введите длину серии для сериального теста шифрования:")
slen=int(input())
serialtest(enc,slen)
print("k=1 для корреляционного теста Rk")
corrtest(enc,1)
print("k=2 для корреляционного теста Rk")
corrtest(enc,2)
print("k=3 для корреляционного теста Rk")
corrtest(enc,3)
print("k=4 для корреляционного теста Rk")
corrtest(enc,4)
print("k=5 для корреляционного теста Rk")
corrtest(enc,5)
print("k=6 для корреляционного теста Rk")
corrtest(enc,6)
print("k=7 для корреляционного теста Rk")
corrtest(enc,7)
print("k=8 для корреляционного теста Rk")
corrtest(enc,8)
print("k= 9 для корреляционного теста Rk")
corrtest(enc,9)
print()
d = open('decrypt.txt', 'r')
dec = d.read()
d.close()
print("Введите длину серии для сериального теста расшифрования:")
slen=int(input())
serialtest(dec,slen)
print("k=1 для корреляционного теста Rk")
corrtest(dec,1)
print("k=2 для корреляционного теста Rk")
corrtest(dec,2)
print("k=3 для корреляционного теста Rk")
corrtest(dec,3)
print("k=4 для корреляционного теста Rk")
corrtest(dec,4)
print("k=5 для корреляционного теста Rk")
corrtest(dec,5)
print("k=6 для корреляционного теста Rk")
corrtest(dec,6)
print("k=7 для корреляционного теста Rk")
corrtest(dec,7)
print("k=8 для корреляционного теста Rk")
corrtest(dec,8)
print("k= 9для корреляционного теста Rk")
corrtest(dec,9)