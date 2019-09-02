import re

#Deni Saputra
def case_email():
	email = re.findall('\S+@\S+',a)
	print(email)

def case_uang():
	email = re.findall('[0-9]+',a)
	b = [int(x)for x in email]	 
	k = re.split(r'\s',a)
	jum = 0
	for i in k:
		if i == "Ribu":
			jum = jum + 1
		elif i == "Juta":
			jum = jum + 2
	if jum == 1:
		print(b[0]*1000)
	elif jum == 2:
		print(b[0]*1000000)
	elif jum == 3:
		print(b[0]*1000000000)

def case_waktu():
	for x in range(0,len(a)):
		if a[x] == ":":
			print(a[x-2:x+3])

print("Test Case: ")
case = input()
print("Masukkan input: ")
a = input()

if case is "1":
	case_waktu()
	 
elif case == "2":
	case_uang()

elif case == "3":
	case_email()

else:
	print("Test Case Tidak Ditemukan")
	


# email = re.findall('\S+@\S',a)
# print(email)