#NIM/Nama : 19622001 / Ricky Wijaya
#Tanggal : 14 September 2022
#Deskripsi : Project 3 (Menentukan waktu lari tuan riz)


# Meminta waktu mulai 
print("Masukan waktu mulai !")
jam0 = int(input("Jam   : "))
menit0 = int(input("Menit : "))
detik0 = int(input("Detik : "))

# Meminta waktu selesai
print("Masukan waktu selesai !")
jam1 = int(input("Jam   : "))
menit1 = int(input("Menit : "))
detik1 = int(input("Detik : "))

# Menghitung Waktu

jam1detik = jam1 * 3600
menit1detik = menit1 * 60

jam0detik = jam0 * 3600
menit0detik = menit0 * 60

detiktotal = (jam1detik + menit1detik + detik1) - (jam0detik + menit0detik + detik0)

jamhasil = detiktotal // 3600
menithasil = (detiktotal % 3600) // 60
detikhasil = ((detiktotal % 3600) % 60)

#invalid
if jam1 > 24 or jam1 < jam0 or jam0 > 24 or menit1 > 60 or menit0 > 60 or detik1 > 60 or detik0 > 60 :
    print("Waktu jam invalid")
    exit()


# Menyusun kalimat output
if jamhasil == 0 :
    print('Tuan riz berlari selama',menithasil,'menit',detikhasil,'detik')
elif menithasil == 0 :
    print('Tuan riz berlari selama',jamhasil,'menit',detikhasil,'detik')
elif detikhasil == 0 :
    print('Tuan riz berlari selama',jamhasil,'jam', menithasil,'menit')    
else : 
    print('Tuan riz berlari selama',jamhasil, 'jam', menithasil, 'menit', detikhasil,'detik')


