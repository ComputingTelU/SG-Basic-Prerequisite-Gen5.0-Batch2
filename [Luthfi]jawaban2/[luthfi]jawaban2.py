a = input("Masukkan input : ")
nospace = a.replace(" ","")
nospace = nospace.replace("Rp","")
stored = a.split()
jam = []
menit = []
dexAt, dexDot = 0, 0
case = 2

#Cek case
for i in range(len(nospace)):
    if (nospace[i]==':'):
        case = 1
        jam.append(nospace[i-2]+nospace[i-1])
        menit.append(nospace[i+1]+nospace[i+2])
    elif (nospace[i]=='@'):
        case = 3
        print(stored)
        break

if (case==1):
    for m in range(len(jam)):
        if (int(jam[m])<=23) and (int(jam[m])>=0) and (int(menit[m])>=0) and (int(menit[m])<=59) :
                print(jam[m]+':'+menit[m])
elif case==2 :
    multiple = 1
    list = []
    for i in range(len(stored)):
        if stored[i]=="Juta":
            multiple = multiple * 1000000
            list.append(stored[i-1])
        elif stored[i]=="Ribu":
            multiple = multiple * 1000
            list.append(stored[i-1])
        elif i==len(stored)-1 :
            sung = False
    if (sung):
        bilangan = int(list[0]) * multiple
        print(bilangan)
    else:
        nospace = nospace.replace(",00","")
        nospace = nospace.replace(".","")
        print(nospace)
        
elif (case==3):
    for k in range(len(nospace)):
        if nospace[k]=='@':
            dexAt = k
        elif nospace[k]=='.':
            dexDot = k
    if (dexAt < dexDot) :
        x = 0
        nemu = False
        while(not nemu) and (x<len(stored)):
            loop = len(stored[x])
            j = 0
            while j<loop:
                if stored[x][j]=="@":
                    print(stored[x])
                    nemu = True
                    j = loop
                j = j+1
            x = x + 1
    else:
        print("Email Tidak Valid")


    
    
    
    
