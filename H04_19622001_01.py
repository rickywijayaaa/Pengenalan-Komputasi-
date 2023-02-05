# NIM / Nama : 19622001 / Ricky Wijaya
# Tanggal : 09 November 2022
# Deskripsi : Program Menentukan nilai terbesar

# Algoritma

n  = int (input("Masukkan nilai N : ")) # Baris
m = int (input("Masukkan nilai M : ")) # Kolom

nilai = [[0 for i in range (m)]for j in range (n)]


for i in range (n):
    for j in range (m):
        nilai[i][j] = int(input(f"Masukkan elemen baris ke {i+1} dan kolom ke {j+1} : "))

for i in range (n):
    sum = 0 
    a = "baris"
    for j in range (m):
        sum = sum + nilai[i][j]
    if i == 0:
        maxnilai = sum
        urutan = i+1 
    else :
        if sum > maxnilai :
            maxnilai = sum
            urutan = i+1


temporarymax = maxnilai  #menyimpan nilai max dari baris
temporaryurutan = urutan # menyimpan urutannya


for i in range (m):
    sum = 0
    a = "kolom"
    for j in range (n):
        sum += nilai[i][j]
    if i == 0 :
        maxnilai = sum
        urutan = i +1
    else:
        if sum > maxnilai :
            maxnilai = sum
            urutan = i+1

print(maxnilai)

if temporarymax > maxnilai:
    maxnilai = temporarymax
    urutan = temporaryurutan
    a = "baris"


print(f"Nilai maksimum sebesar {maxnilai} pada {a} ke {urutan} ")