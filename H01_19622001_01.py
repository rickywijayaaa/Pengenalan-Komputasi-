# NIM/Nama : 19622001/Ricky Wijaya
# Tanggal : 14 September 2022
# Deskripsi : Project 1 Menentukan barang yang ditawarkan (keuntungan terbesar)

# Masukkan nilai
HJA = float(input(("Masukkan Harga Jual Barang A: ")))
HBA = float(input(("Masukkan Harga Beli Barang A: ")))
HJB = float(input(("Masukkan Harga Jual Barang B: ")))
HBB = float(input(("Masukkan Harga Beli Barang B: ")))
HJC = float(input(("Masukkan Harga Jual Barang C: ")))
HBC = float(input(("Masukkan Harga Beli Barang C: ")))

# Menghitung Laba Yang Diperoleh
KA = (HJA - HBA)
KB = (HJB - HBB)
KC = (HJC - HBC)

# Mengurutkan Keuntungan Terbesar
if (KA > KB > KC) :
    print("Tawarkan Barang A")
elif (KA > KC > KB) :
    print("Tawarkan Barang A")
elif (KB > KA > KC) :
    print("Tawarkan Barang B")
elif (KB > KC > KA) :
    print("Tawarkan Barang B")
elif (KC > KA > KB) :
    print("Tawarkan Barang C")
else :#KC > KB > KA
    print("Tawarkan Barang C")