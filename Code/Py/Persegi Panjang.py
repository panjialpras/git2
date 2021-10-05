print("==========Luas dan Keliling Persegi Panjang==========")

p = str(input("masukkan panjangnya: "))
l = str(input("masukkan lebarnya: "))

luas = p * l
pilih = input("1. Luas, 2. Keliling")

if (pilih == "1") :
    print("1. Luas adalah ", luas)
else: keliling = 2 * p + l
    print("2. Keliling adalah ", luas)