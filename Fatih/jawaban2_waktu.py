import re

Text = ""

while True :
	try :
		Text += input() + '\n'
	except EOFError :
		break
		
print(Text)

Match = re.findall(r'\d{2}:\d{2}', Text)

print(Match)
	
	