# NIM / Nama : 19622001 / Ricky Wijaya
# Tanggal : 18 Oktober 2022
# Deskripsi : Program Lampu

# Algoritma
banyak = int(input("Masukkan banyak lampu: "))
tekan = int(input("Masukkan berapa kali Tuan Kil menekan tombol: "))

arr = [0 for i in range (banyak)]
for i in range(tekan):
    tombol = int(input(f"Tombol yang ditekan ke {i+1}: "))
    tombol = tombol - 1
    if arr[tombol] == 0:
        arr[tombol] = 1
    else:
        arr[tombol] = 0

    if tombol - 1 >= 0:
        if arr[tombol-1] == 0 :
            arr[tombol-1] = 1
        elif arr[tombol-1] == 1:
            arr[tombol-1]= 0
    
    if tombol + 1 <= banyak -1 :
        if arr[tombol+1] == 0 :
            arr[tombol+1] = 1
        elif arr[tombol+1] == 1:
            arr[tombol+1]= 0

print ("Keadaan akhir rangkaian lampu adalah ", end=" ")
for i in range (banyak):
    print(arr[i], end="")