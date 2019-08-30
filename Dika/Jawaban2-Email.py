import re

text = ''

while True:
    try:
        text += input()
    except EOFError:
        break

email = re.findall(r'[\S\.-]+@[\S\.-]+\.\S+', text)

print(email)
