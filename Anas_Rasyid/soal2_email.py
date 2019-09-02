import re
sentece = ''
while True:
    try:
        sentece += input()
    except EOFError:
        break
pattern = '\S+@\S+[.]\S+'
match = re.findall(pattern, sentece)
print(match)