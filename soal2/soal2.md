Diberikan inputan berupa sebuah kata dan dilanjutkan sebuah kalimat. Anda harus mengambil objek yang ada pada kalimat tersebut berdasarkan kata yang dimasukkan pertama.

Gunakan input dari file soal2-testcase.txt

Case 1 (Waktu):
Waktu didefinisikan sebagai 4 digit bilangan bulat yang mana ditengahnya terdapat ':'. Dua digit pertama adalah bilangan antara 0-23, Sedangkan dua digit setelah ':'  adalah bilangan antara 0-59.
Contoh: 03:15, 12:02
Input:
Ada kereta gak jadwal jam 03:00 arah bandung jakarta?
Output:
03:00

Case 2 (Uang):
Uang didefinisikan sebagai sebuah bilangan (tidak selalu integer) pada suatu kalimat. Apabila ada kata 'ribu' atau 'juta' (Upper/Lower) maka objek uang tersebut akan dikalikan dengan 10^3 atau 10^6. Apabila salah satu dari kedua kata itu, maka nilai outputnya langsung berdasarkan objek uang tersebut.
Contoh: 5 Ribu, 30000, 1.5 juta
Input:
HP Ram 2 GB yang harganya dibawah Rp. 3 juta
Output:
3000000

Case 3 (Email):
Email terdefinisikan sebuah kata dimana ditengah kata itu terdapat '@' dan '.', Dimana character '@' selalu mendahului character '.' . Diantara '@' dan '.' terdapat sebuah string dengan panjang bebas.
Contoh: abcdef@ghijk.com, a@f.s
Input:
Kirim ke Emailnya testcase@gmail.com
Output:
testcase@gmail.com