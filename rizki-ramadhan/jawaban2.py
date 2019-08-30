def waktu(kalimat):
    kalimat = kalimat.replace(","," ")
    kalimat = kalimat.replace(".","")
    kata = kalimat.split()
    for k in kata:
        if ":" in k:
            test = k.split(":")
            if int(test[0]) <= 23 and int(test[1])<=59:
                print(k)

def uang(kalimat):
    kalimat = kalimat.replace(",00","")
    kalimat = kalimat.replace("Rp","")
    kalimat = kalimat.replace(".","")
    kalimat = kalimat.lower()
    kata = kalimat.split()
    i=0
    for i, item in enumerate(kata):
        if "ribu" in item and ((kata[i-1] != "ribu") and (kata[i-1] != "juta")):
            print(int(kata[i-1])*1000)
        elif "juta" in item and ((kata[i-1] != "ribu") and (kata[i-1] != "juta")):
            print(int(kata[i-1])*1000000)
        elif "000" in kata[i]:
            print(kata[i])
def email(kalimat):
    kata = kalimat.split()
    for k in kata:
        if (k.find('@') < k.find('.')) and k.find('@')!=-1 :
            print(k)

if __name__ == "__main__":
    kalimat = input("Masukkan Testcase: ")
    if ":" in kalimat:
        waktu(kalimat)
    elif "@" in kalimat:
        email(kalimat)
    else:
        uang(kalimat)