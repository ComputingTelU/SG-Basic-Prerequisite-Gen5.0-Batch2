import time

def isTimeFormat(input):
    try:
        time.strptime(input, '%H:%M')
        return True
    except ValueError:
        return False

def split_line(text):

    words = text.split(" ")

    for word in words:
        if isTimeFormat(word):
            print(word)

word = """Tengah malam adalah pada pukul 00:00.
Study Group Basic akan diadakan pada pukul 19:00 hingga 21:00 pada hari Rabu.
Kereta akan melewati stasiun Bandung pada pukul 00:11, 06:30, 13:45, dan 23:59.
Adikku baru belajar menulis waktu, kemarin. Dia salah menuliskan waktu yang seharusnya 23:59 menjadi 25:69."""
split_line(word)