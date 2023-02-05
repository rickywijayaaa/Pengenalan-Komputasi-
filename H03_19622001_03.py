# NIM / Nama : 19622001 / Ricky Wijaya
# Tanggal : 18 Oktober 2022
# Deskripsi : Program menghitung banyak kemunculan sebuah substring pada string lain.

# Algoritma

n1 = int(input("Masukkan panjang string 1: "))
st1 = str(input("Masukkan string 1: "))

n2 = int(input("Masukkan panjang string 2: "))
st2 = str(input("Masukkan string 2: "))

sum = 0

for i in range(n2-n1 + 1):
    x= 0
    for j in range (n1):
        if st1[j] == st2[i]:
            x = x + 1
        i = i + 1
    if x == n1 :
        sum = sum + 1

print("String 1 muncul sebanyak", sum, "kali")