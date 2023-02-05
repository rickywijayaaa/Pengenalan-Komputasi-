# NIM / Nama : 19622001 / Ricky Wijaya
# Tanggal : 09 November 2022
# Deskripsi : Program Mengecek serangan kuda

#Algoritma

m = int (input("Masukkan nilai m : "))

catur = [[0 for i in range (m)]for j in range (m)]

for i in range(m):
    for j in range (m):
        catur[i][j] = input(f"Masukkan elemen matriks ke-{i+1} {j+1} :  ")
        if catur[i][j] == 'R' :
            x = i 
            y = j


cek = True

for i in range (m):
    for j in range (m):
        if (i==x-2 or i == x+2) and (j == y-1 or j== y+1):
            if catur[i][j] == "K":
                cek = False
        if (i==x-1 or i == x+1) and (j == y-2 or j== y+2):
            if catur[i][j] == "K":
                cek = False 
if cek == False:
    print("Raja tidak aman dari serangan kuda")
else:
    print("Raja aman dari serangan kuda")