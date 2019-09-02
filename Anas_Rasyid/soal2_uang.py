import re
sentece = ''
while True:
    try:
        sentece += input()
    except EOFError:
        break
pattern = '\S+'
match = re.findall(pattern, sentece.lower())
ans = []
i = 0
word = len(match)
while i < word:
  tmp = re.findall('\d+[.]\d+|\d+',match[i])
  if(len(tmp) != 0):
    tmp[0] = tmp[0].replace('.','')
    nilai = int(tmp[0])
    if(match[i + 1] == 'ribu'):
      nilai *= 1000
      i = i + 1
    elif(match[i + 1] == 'juta'):
      nilai *= 1000000
      i = i + 1
    if(i + 1 >= word) or(match[i + 1] != 'juta' and match[i + 1] != 'ribu' and nilai > 10):
      ans.append(nilai)
  i = i + 1
print(ans)