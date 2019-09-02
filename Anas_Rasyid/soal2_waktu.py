import re
sentece = ''
while True:
    try:
        sentece += input()
    except EOFError:
        break
pattern = '[0-9][0-9]:[0-9][0-9]'
match = re.findall(pattern, sentece)
print(match)