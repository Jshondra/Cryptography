from generator import gen_prime
from generator import gen_not_prime
from generator import gen_prime_test
from attack import attack
from encryption import encryption
from decryption import decryption
import random
import time
# from rmspp import mode

print("Введите длину ключа L(128,256,512 bit): ")
L = int(input())
if L not in [128,256,512]:#Проверка на размер
    print("Неверное значение!")
    raise SystemExit
#Создание N,e,d и запись их в файл.txt
gen_prime(L)
# mode(L, 10)
#Считывание строки
print("Введите строку")
text = input()
if len(text) > L/8:#Проверка на размер
    print("Строка должна быть меньше ",int(L/8)," символов!")
    raise SystemExit
arg = ""
while arg != '7':
    print("_______________________________")
    print("Выберите действие:")
    print("1-Зашифровать строку")
    print("2-Расшифровать строку")
    print("3-Использовать простые числа(p,q)")
    print("4-Атака!")
    print("5-Сгенерировать новый L(Для проверки атаки)")
    print("6-5 Задание")
    print("7-Выход")
    print("_______________________________")
    arg = input()
    if arg == '1':
        encryption(text,L)
    elif arg == '2':
        decryption(L)
    elif arg == '3':
        gen_not_prime(L)
    elif arg == '4':
        start_time = time.time()
        attack()
        print("--- %s секунд (время факторизации)" % (time.time() - start_time))
    elif arg == '5':
        print("Введите длину ключа L: ")
        L = int(input())
        gen_prime(L)
    elif arg == '6':
        r = 0.25
        L = 90#L для 5 задания
        while r < 0.5:
            gen_prime_test(L,r)
            start_time = time.time()
            attack()
            print("--- %s секунд (время факторизации)" % (time.time() - start_time))
            print("r = ",round(r,2))
            print("_______________________________")
            r += 0.05
    elif arg == '7':
        print("Exit")
    else:
        print("Не верное значение!")