# NIM / Nama : 19622001 / Ricky Wijaya
# Tanggal : 09 November 2022
# Deskripsi : Program Membuat bilangan komposit

#Algoritma

def is_prima(n):              # Program menentukan prima
    for i in range(2,n):
        if (n%i) == 0:
            return False
    return True

def is_komposit(n):          # Program menentukan komposit
    if n == 1 :
        return False
    else:
        return not is_prima(n)

def is_pasangan_komposit (a , b): # Program menentukan pasangan komposit
    return is_komposit(a) and is_komposit(b) and is_komposit(a+b)

A = int (input("Masukkan A : "))    # Meminta input     
B = int (input("Masukkan B : "))

print("Pasangan bilangan komposit : ")
for i in range (A , B+1) :            # Untuk mengecek bilangan pertama
    for j in range (i+1 , B+1):       # Untuk mengecek bilangan kedua
        if is_pasangan_komposit(i,j):
            print(i,j)                  # Output