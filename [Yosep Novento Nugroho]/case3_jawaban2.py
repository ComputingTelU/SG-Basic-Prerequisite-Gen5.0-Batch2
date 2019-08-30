import re


def searchemail(input):
    words = input.split(" ")

    for word in words:
        email = re.findall("([a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+)", word)

        if len(email) != 0:
            print(' '.join(email))




text = """ini email lab lab-computing@telkomuniversity.ac.id .
va@li.d adalah contoh email yang valid.
tidak@valid dan tidak.valid adalah tidak valid.
dan ini tidak.valid@juga"""


searchemail(text)