import re


def convstrtonumb(text):
    out = re.sub(r'(?i)\b(\d+) ?j(?:j|uta?)?\b', r'\g<1>000000', text)
    out2 = re.sub(r'(?i)\b(\d+) ?r(?:r|ibu?)?\b', r'\g<1>000', out)
    words = out2.split(" ")

    for word in words:
        x = re.findall('\d+', word)
        if len(x) != 0:
            print(' '.join(x))


text = """Aku memiliki uang 90 Ribu Rupiah.
Aset lab Computing totalnya bernilai sekitar 300 Juta Rupiah.
Rp12.000,00
3 Ribu Juta bukanlah nominal yang valid."""


convstrtonumb(text)