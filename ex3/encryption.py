from helper import dec_to_bin
from helper import quick

def encryption(text,L):#Шифрование строки в двоичную последовательность С, text - строка ,
    # L - длина ключа
    tbin_array = [ord(k) for k in text]#Перевод символов в кодировку ascii
    for i in range(len(tbin_array)):#Перевод ascii в двоичный код
        tbin_array[i] = dec_to_bin(tbin_array[i])
    i=0#Выравниваем блоки по размеру = L/4
    if len(text) % (L/32) != 0:
        while i < (L/32)-len(text) % (L/32):
            tbin_array.append(0)
            i +=1
    string = ""#Преобразуем в строку M
    for i in range(len(tbin_array)):
        if tbin_array[i] == 0:
            string += "00000000"
        elif tbin_array[i] < dec_to_bin(64):
            string += "00"
            string += str(tbin_array[i])
        else:
            string += "0"
            string += str(tbin_array[i])
    #print("M : ",string)
    l=len(tbin_array)*8
    M_array = tbin_array
    M_array.clear()
    temp = ""
    i=0#Разбираем на блоки по L/4 бита
    while i < l:
        temp += string[i]
        if len(temp) == L/4:
        #print("-",len(temp),"-",temp)
            M_array.append(int(temp,2))
            temp = ""
        i +=1
    #print("M в dec :",M_array)
    #Чтение значений e и N
    Fin = open ("/mnt/e/crypto/public.txt", "r" )
    temp_string = Fin.read()
    Fin.close
    temp_array = [int(s) for s in temp_string.split() if s.isdigit()]
    e = int(temp_array[0]); N = int(temp_array[1])
    lenN =len(bin(N)[2:])
    #print("Размер N:",lenN)
    C_array=[]
    s = len(M_array)
    i = 0
    while i < s:#Шифруем С = M^e mod N и сразу в двоичный код
        C_array.append( bin(quick(int(M_array.pop(0)),e,N))[2:])
        temp = lenN - len(C_array[i])
        C_array[i] = "0"*temp + C_array[i]
        i+=1
    string2 = ""
    i=0
    while i < s:
        string2 += str(C_array.pop(0))
        i+=1
    #print("С :",string2)
    #Запись в файл C
    Fout = open ( "/mnt/e/crypto/encrypted.txt", "w" )
    Fout.write(string2)
    Fout.close()