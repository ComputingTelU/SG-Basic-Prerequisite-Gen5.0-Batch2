import re

inputan = str(input()) 

def cari_waktu(inputan):
    print(re.findall("[0-23][0-59]:[0-23][0-59]", inputan))
    

def cari_uang(inputan):
    juta = re.sub("juta|JUTA|Juta","000000",inputan)
    ribu = re.sub("ribu|RIBU|Ribu","00000", juta)
    hasil = re.findall("[0-99999999999]",ribu)

    for cobain in hasil:
        print(cobain)


def cari_email(inputan):
    meki = "zetaraehan@gmail.com"
    tol = re.findall("([a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+)",meki)
    print(tol)
    
cari_waktu(inputan)
cari_uang(inputan)
cari_email(inputan)