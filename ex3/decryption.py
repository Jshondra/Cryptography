from helper import quick
def decryption(L):
#Чтение encrypted
    Fin = open ("/mnt/e/crypto/encrypted.txt", "r" )
    C_array = Fin.read()
    Fin.close
    #Чтение значений d и N
    Fin = open ("/mnt/e/crypto/private.txt", "r" )
    temp_string = Fin.read()
    Fin.close
    temp_array = [int(s) for s in temp_string.split() if s.isdigit()]
    d = int(temp_array[0]); N = int(temp_array[1])
    lenN =len(bin(N)[2:])
    i=0#Разбиваем С
    C =[]
    temp = ""
    while i < len(C_array):
        temp += C_array[i]
        if len(temp) == lenN:
            C.append(bin(quick(int(temp,2),d,N))[2:])#Расшифровка M=C^d mod N
            temp = ""
        i +=1

    i=0
    temp_string = ""
    while i < len(C):
        a = int(L/4)-len(C[i])
        C[i] = "0"*a+ C[i]
        temp_string += C[i]
        i+=1
    #print("string:",temp_string)
    temp = ""
    i=0
    D=[]#Преобразоваваем bin -> ascii(код)
    while i < len(temp_string):
        temp +=temp_string[i]
        if len(temp) == 8:
            D.append(int(temp,2))
            temp = ""
        i +=1
    #print("D :",D)
    S =""#S - расшифрованная строка
    k =0
    while k < len(D):
        S += chr(D[k])
        k +=1
    print("Расшифрованная строка:",S)
    Fout = open ( "/mnt/e/crypto/decrypted.txt", "w" )
    Fout.write(S)
    Fout.close()