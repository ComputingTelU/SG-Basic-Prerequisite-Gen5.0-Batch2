import re

Text = ""

while True :
	try :
		Text += input() + '\n'
	except EOFError :
		break
		
print(Text)

Match = re.findall(r'([1-9]\d{0,2}(\.\d{3})?(\s[a-zA-Z]+){0,2})', Text)

Raw = []
for i in Match :
	Raw.append(i[0].split())
	

print(Raw)
	
List = []

for i in Raw :
	
	#print(i)
	
	Valid = True
	if len(i) == 3 :
		if i[2].lower() in ['juta', 'ribu'] :
			Valid = False
		else :
			i.pop()
		
	if Valid and len(i) == 2 :
		if i[1].lower() == 'rupiah' :
			i.pop()
		elif i[1].lower() not in ['juta', 'ribu'] :
			Valid = False
			
	i[0] = i[0].replace('.', '')
	
	i[0] = i[0].replace(',', '.')
	
	if Valid :
		List.append(i)

for i in List :
	Result = float(i[0])
	if len(i) == 2 :
		if i[1].lower() == 'juta' :
			Result *= 1000000
		else :
			Result *= 1000
	
	print(int(Result))
"""
Aku memiliki uang 90 Ribu Rupiah.
Aset lab Computing totalnya bernilai sekitar 300 Juta Rupiah.
Rp12.000,00
3 Ribu Juta bukanlah nominal yang valid.
HP Ram 2 GB yang harganya dibawah Rp. 3 juta
200 rupiah
"""