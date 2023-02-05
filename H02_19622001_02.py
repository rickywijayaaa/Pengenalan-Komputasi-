# NIM / Nama : 19622001/ Ricky Wijaya
# Tanggal : 04 Oktober 2022
# Deskripsi : Program Bilangan Membesar

# KAMUS
# N  = integer
# sum = integer
# prev_number = integer
# first_number = integer
# Algoritma

count_tidak = 0 
sum = 0

first_number = int(input("Angka ke-1: "))
prev_number = first_number
n = 2

while count_tidak < 3: 
    angka = int(input(f"angka ke-{n}: "))

    if angka > prev_number :
        sum +=  angka
        count_tidak * 0 
    elif angka < prev_number :
        count_tidak += 1
    
    n += 1
    prev_number = angka

print (f"Jumlah nilai yang membesar adalah: {sum}")


    