import random
import math

alphabet='абвгдеёжзийклмнопрстуфхцчшщъыьэюя '
def reverse_string1(s):
	return s[::-1]

def entropy(text):
	sum = 0
	alph_list = ['а', 'б', 'в', 'г', 'д', 'е', 'ё', 'ж', 'з', 'и', 'й', 'к', 'л', 'м', 'н', 'о', 'п', 'р', 'с', 'т', 'у',
			'ф', 'х', 'ц', 'ч', 'ш', 'щ', 'ъ', 'ы', 'ь', 'э', 'ю', 'я', ' ']
	for i in range(len(alph_list)):
		pi = text.count(text[i])/len(text)
		sum += math.log2(pi)*pi
	sum = (-sum)

	print("Энтропия алфавита=",sum)

def keygen(alphabet):
	with open('key.txt', mode = 'w') as file:
		key = ''.join(random.sample(alphabet, len(alphabet)))
		file.write(key)
	return key

def encrypt(alphabet):
	k = keygen(alphabet)
	d = dict()
	res=""
	for i in range(len(alphabet)):
		d[alphabet[i]] = k[i]
	with open('file.txt') as f:
		read_data = f.read().strip()
		for i in range(len(read_data)):
			if read_data[i] in d:
				res += d[read_data[i]]
			else: res += read_data[i]
	with open('output.txt', 'w') as o:
		o.write(res)
	entropy(res)

def decrypt1(alphabet):
	with open('key.txt') as f:
		k = f.read().strip()
	d = dict()
	res = ""
	for i in range(len(alphabet)):
		d[k[i]] = alphabet[i]
	with open('output.txt') as f:
		read_data = f.read().strip()
		for i in range(len(read_data)):
			if read_data[i] in d:
				res += d[read_data[i]]
			else:
				res += read_data[i]
	with open('file2.txt', 'w') as o:
		o.write(res)
	entropy(res)

	
def decrypt2(alphabet):
	d = dict()
	s = " оеаитнсрвлкмдпуяызьъбгчйхжюшцщэф"
	res = ""
	with open('output.txt') as f:
		read_data = f.read().strip()
		for i in range(len(read_data)):
			d[read_data[i]] = read_data.count(read_data[i])
	list_d = list(d.items())   
	list_d.sort(key=lambda i: i[1])
	list_d = reverse_string1(list_d)
	for i in range(len(s)):
		list_d[list_d[i]] = s[i]
		for i in range(len(read_data)):
			if read_data[i] in d:
				res+=d[read_data[i]]
			else: res+=read_data[i]
	print(res)


	print (list_d)

			#res +=  d[i]
	# with open('/mnt/e/School21/file3.txt', 'w') as o:
	#     o.write(d)
	print(d)

def decrypt3():
	freq = dict()
	sum=""
	alph_list = ['а', 'б', 'в', 'г', 'д', 'е', 'ё', 'ж', 'з', 'и', 'й', 'к', 'л', 'м', 'н', 'о', 'п', 'р', 'с', 'т', 'у',
			'ф', 'х', 'ц', 'ч', 'ш', 'щ', 'ъ', 'ы', 'ь', 'э', 'ю', 'я', ' ']
	freq_russian = ' оеаитнсрвлкмдпуяызъьбгчйхжюшцщэф'
	with open('file2.txt') as outp:
		read_decr = outp.read().strip()
		read_decr=read_decr.lower()
		sum+=read_decr
		for i in range(len(read_decr)):
			if read_decr[i] in alph_list and read_decr[i] not in freq:
				freq[read_decr[i]]= sum.count(read_decr[i])/len(sum)
	# print(freq)
	# print(len(sum))
	sorted_freq=dict(sorted(freq.items(), key=lambda item: item[1]))
	print(sorted_freq)

	letters=""
	for i in reversed(sorted_freq.keys()):
		letters+=i
	print("Частоты букв русского алфавита",freq_russian)
	print("Частоты букв шифрограммы",letters)
	table = dict()
	for i in range(len(letters)):
		table[letters[i]]=freq_russian[i]

	table['ь'] = 'а'
	table['щ'] = 'и'
	table['д'] = 'н'
	table['м'] = 'с'
	table['ж'] = 'о'
	table['й'] = 'в'
	table['а'] = 'п'
	table['г'] = 'т'
	table['х'] = 'е'
	table['з'] = 'л'
	table['ц'] = 'ь'
	table['о'] = 'з'
	table['в'] = 'ж'
	table['к'] = 'я'
	table['т'] = 'х'
	table['ч'] = 'д'
	table['ы'] = 'м'
	table['я'] = 'к'
	table['ф'] = 'ю'
	table['н'] = 'ы'
	table['и'] = 'ч'
	table['п'] = 'г'
	table['л'] = 'й'
	table['б'] = 'ц'
	table['р'] = 'э'
	table[' '] = 'б'
	
	s = "Зашифрованный алфавит- расшифрованный алфавит\n"
	for v,k in table.items():
		s += v + " - " + k + '\n'
	res=""
	with open('table.txt', 'w') as o:
		o.write(s)
	with open('file2.txt') as f:
		read_data = f.read().strip()
		read_data=read_data.lower()
		for i in range(len(read_data)):
			if read_data[i] in alphabet:
				res+=table[read_data[i]]
			else: res+=read_data[i]
	with open('decrypt.txt', 'w') as o:
		o.write(res)
	entropy(res)

str=input("Введитие 1 для зашифрования, либо 2 для дешифрования, либо 3 для частотного анализа:\n")
if str=="1":
   print("Задание 1, шифрование")
   encrypt(alphabet)
elif str=="2":
   print("Задание 1, дешифрование")
   decrypt1(alphabet)

elif str=="3":
   print("Задание 2, частотный анализ")
   decrypt3()
