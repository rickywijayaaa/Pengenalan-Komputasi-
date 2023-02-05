# NIM / Nama : 19622001 / Ricky Wijaya
# Tanggal : 18 Oktober 2022
# Deskripsi : Program menentukan diskon


n = int(input("Masukkan banyak barang: "))
arr = [0 for i in range(n)]
max = 0
count = 0 

for i in range (n):
    arr[i] = int(input(f"Masukkan harga awal ke- {i+1}: "))
for i in range(n):
    diskon = int(input(f"Masukkan besar diskon (dalam persen) barang ke- {i+1}: "))
    arr[i] = arr[i] * diskon // 100
for i in range(n):
    if i == 0 :
        count = i + 1
    if arr[i] > arr[i-1]:
        max = arr[i]
        count = i + 1
print(f"Barang {count} memiliki diskon paling besar yaitu {max}.")