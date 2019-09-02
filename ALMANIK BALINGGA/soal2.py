#maap kalo ngodingnya bar bar

def waktunya(b):
    #kita pecah jadi beberapa bagian
    nani = b.split()
    #looping
    for i in range(len(nani)) :
        #ubah elemn list jadi string
        aa = str(nani[i])
        #ada elemen ':' gak didalemnya
        if ':' in aa :
            #kalo ada udahan
            break
    #ini sesuai format waktu JJ:MM gak?        
    if (len(aa)==5):
        #cek format
        c = int(aa[0])
        d = int(aa[3])
        #kalo bener yaaa
        if (c < 3) & (d<7):
            #di return
            return print(aa)
        else:
            #kalo salah sans
            return print("PERGI SAJA PERGI DARI HIDUPKU")
        
def emailnya(b):
    # di split, ntah kenapa tapi pengen aja
    nani = b.split()
    #ulang
    for i in range(len(nani)) :
        #jadiin string
        aa = str(nani[i])
        #ini ada @ nya gak?
        if '@' in aa :
            #kalo ada oke
            break
    # ada @ belom tentu email        
    c = aa.split('@')
    # ada titik gak abis @?
    if '.' in str(c[1]) :
        #kalo ada bener berarti
        return print(aa)
    else:
        # kalo bukan nyanyi lagi
        return print("BIAR KUBUNUH PERASAAN UNTUKMU")
    
    
def uangnya(b):
    #kita pecah jadi beberapa bagian
    nani = b.split()
    #looping
    for i in range(len(nani)) :
        #ubah elemn list jadi string
        aa = str(nani[i])
        #ada elemen '0' gak didalemnya
        if ('0' in aa):
            #kalo ada ya oke
            break
            #kalo gada lanjut
        # ada kata juta ato ribu gak?    
        elif (aa.lower()=="juta") or (aa.lower()=="ribu") :
            #kalo ada cari nominal nya
            c = int(nani[i-1])
            break
            #kalo ada oke beres ulang
    #kalo udah eksplisit langsung gas       
    if('0' in aa):
        return print(aa)
    #kalo juta ubah dulu
    elif (aa.lower()=="juta") :
        return print(c*1000000)
    #kalo ribu ubah dulu
    elif (aa.lower()=="ribu") :
        return print(c*1000)
    else:
        #kalo masih gaada nyanyi lagi
        return print("MESKI BERAT MELANGKAH")

    
    
# helo word nya
print("Mau Apa? : ")
#input mau apa
a = input()
#test case
print("Kalimatnya?")
kal = input()
if (a.lower()=="waktu") :
    waktunya(kal)
elif(a.lower()=="email"):
    emailnya(kal)
elif(a.lower()=="uang"):
    uangnya(kal)

