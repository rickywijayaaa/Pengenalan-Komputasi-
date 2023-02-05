# NIM/Nama : 19622001/Ricky Wijaya
# Tanggal : 14 September 2022
# Deskripsi : Project 2 Menentukan Kelas Dari NIM

# Masukkan 3 angka terakhir NIM
NIM = int(input(("Masukkan Akhiran NIM: ")))

# Menentukan kelas
if NIM % 2 == 1 and NIM <= 100 :
    print("Mahasiswa Masuk ke kelas K1")
elif NIM % 2 == 0 and NIM <= 100 :
    print("Mahasiswa Masuk ke kelas K2")
elif NIM % 2 ==  1 and 100 < NIM <= 200 :
    print("Mahasiswa Masuk ke kelas K3")
elif NIM % 2 == 0 and 100 < NIM <= 200 :
    print("Mahasiswa Masuk ke kelas K4")
elif NIM % 2 == 1 and 200 < NIM <= 300 :
    print("Mahasiswa Masuk ke kelas K5")
elif NIM % 2 == 0 and 200 < NIM <= 300 :
    print("Mahasiswa Masuk ke kelas K6")
elif NIM % 2 == 1 and NIM > 300 :
    print("Mahasiswa Masuk ke kelas K7")
else: #NIM % 2 == 0 and NIM > 300 :
    print("Mahasiswa Masuk ke kelas K8")