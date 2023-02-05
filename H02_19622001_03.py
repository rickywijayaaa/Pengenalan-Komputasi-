# NIM / Nama : 19622001/ Ricky Wijaya
# Tanggal : 04 Oktober 2022
# Deskripsi : Program Faktor Prima

# KAMUS
# faktor_pertama = boolean
# N = integer

# Algoritma
N = int(input("Masukkan N: "))
faktor_pertama = False

print("Faktor primanya adalah", end=" ")
for i in range (1,N+1):
    count_faktor = 0
    if (N%i == 0):
        for j in range (1, i+1):
             if (i%j == 0):
                    count_faktor += 1
        if (count_faktor == 2) :
            if (faktor_pertama == False):
                faktor_pertama = True
                print(i, end="")
            else :
                print(f", {i}", end="")
print(".")