def isWaktu(x):
  listwaktu = list(x)
  contains = ":" in listwaktu
  if contains == True :
    return True
  else:
    return False

def isEmail(x):
  listEmail = list(x)
  contains = "@" in listEmail
  contains = "." in listEmail
  ind1 = listEmail.index("@")
  ind2 = listEmail.index(".")

  if contains == True and ind1 < ind2 :
    return True
  else:
    return False


def isfloat(x):
    try:
        float(x)
        return True
    except:
        return False

def isRp(x):
  contains = "Rp" in x
  if contains == True :
    return True
  else:
    return False 


kalimat = input("masukkan kalimat: ")
kalimat2 = kalimat.replace(',' , ' ')
kata = kalimat2.split()
listkata = list()
i = 0 
for kata[i] in kata:
  if isWaktu(kata[i]):
    listkata.append(kata[i])
  elif kata[i] == "Juta":
    listkata[i-1] = int(listkata[i-1])*1000000 
  elif kata[i] == "Ribu":
    listkata[i-1] = int(listkata[i-1])*1000
  elif isRp(kata[i]):
    listkata.append(kata[i].replace("Rp",""))
  elif isfloat(kata[i]):
    listkata.append(kata[i])
  elif isEmail(kata[i]):
    listkata.append(kata[i])
  else :
    print("not valid")

    
print(listkata)

