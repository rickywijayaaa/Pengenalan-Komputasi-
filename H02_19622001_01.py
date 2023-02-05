# NIM / Nama : 19622001/ Ricky Wijaya
# Tanggal : 04 Oktober 2022
# Deskripsi : Program Bilangan Sempurna

# KAMUS
# bilangan = integer 
# Jum_Total = integer

# Algoritma

# Memasukan Input
bilangan = int(input("Masukkan Bilangan:"))
Jum_Total = 0


# Mencari jumlah faktor-faktor dari suatu bilangan
for faktor in range (bilangan-1 , 0 , -1):
    if(bilangan % faktor == 0):
        Jum_Total += faktor

# Output
if(Jum_Total == bilangan):
    print ("Bilangan tersebut adalah bilangan sempurna")
else:
    print("Bilangan tersebut bukan bilangan sempurna")