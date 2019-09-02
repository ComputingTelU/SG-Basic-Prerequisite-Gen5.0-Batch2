f = open('/Users/syiti/Documents/Repository/SG-Basic-Prerequisite-Gen5.0-Batch2/Syiti Liviani/soal2-testcase.txt', 'r')

line = f.readlines()

words = []

y = 0

while y < len(line):
    words.append(line[y].split())
    y = y + 1

#waktu
print("TEST CASE 1")
barisW = 0
while barisW < len(line):
    kataW = 0
    if words[barisW] == []:
        barisW = len(line)
    elif "Test" in words[barisW][kataW]:
        barisW = barisW + 1
    else:
        while (kataW < len(words[barisW])):
            if ":" in words[barisW][kataW]:
                if ("." in words[barisW][kataW]):
                    print(words[barisW][kataW].replace('.',''))
                elif ("," in words[barisW][kataW]):
                    print(words[barisW][kataW].replace(',',''))
                else:
                    print(words[barisW][kataW])
            kataW = kataW + 1
        barisW = barisW + 1

#uang
print("")
print("TEST CASE 2")
barisU = 0
while barisU < len(line):
    kataU = 0
    if words[barisU] == []:
        barisU = barisU + 1
    elif "Test" in words[barisU][kataU]:
        barisU = barisU + 1
    else:
        while (kataU < len(words[barisU])):
            if ("Juta" in words[barisU][kataU] and "Ribu" in words[barisU][kataU+1]) or ("juta" in words[barisU][kataU] and "ribu" in words[barisU][kataU+1]) :
                kataU = len(words[barisU])
            elif ("Ribu" in words[barisU][kataU] and "Juta" in words[barisU][kataU+1]) or ("ribu" in words[barisU][kataU] and "juta" in words[barisU][kataU+1]):
                kataU = len(words[barisU])
            elif "Rp" in words[barisU][kataU]:
                uang = words[barisU][kataU].replace('Rp','')
                uang = uang.replace('.','')
                uang = uang.replace(',','')
                print(uang)
                kataU = kataU + 1
            else:
                if "ribu" in words[barisU][kataU] or "Ribu" in words[barisU][kataU]:
                    print(int(words[barisU][kataU-1])*1000)
                elif "juta" in words[barisU][kataU] or "Juta" in words[barisU][kataU]:
                    print(int(words[barisU][kataU-1])*1000000)
                kataU = kataU + 1
        barisU = barisU + 1

#email
print("")
print("TEST CASE 3")
barisE = 0
while barisE < len(line):
    kataE = 0
    while kataE < len(words[barisE]):
        if "@" in words[barisE][kataE]:
            email = words[barisE][kataE]
            count = 0
            while (count < len(email)):
                if "@" in email[count]:
                    count = count + 2
                    while (count < len(email)):
                        if "." in email[count]:
                            print(words[barisE][kataE])
                            count = len(email)
                        else:
                            count = count + 1
                else:        
                    count = count + 1
            kataE = len(words[barisE])
        else:
            kataE = kataE + 1   
    barisE = barisE + 1

f.close()