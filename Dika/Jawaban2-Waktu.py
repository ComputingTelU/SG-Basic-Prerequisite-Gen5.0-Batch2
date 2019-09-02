import re

text = ''

while True:
    try:
        text += input()
    except EOFError:
        break

time = re.findall('[0-1][0-9]:[0-5][0-9]', text)
time += re.findall('[2][0-4]:[0-5][0-9]', text)

print(time)
