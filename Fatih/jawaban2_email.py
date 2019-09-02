import re

Text = ""

while True :
	try :
		Text += input() + '\n'
	except EOFError :
		break
		
print(Text)

Match = re.findall(r'[^@\s]+@[^@\s]+\.[^@\s]+', Text)

print(Match)