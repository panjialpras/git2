print("Menghitung Gaji Karyawan")

print("1. Karyawan Tetap")
print("2. Karyawan Tidak Tetap")
pilih = str(input("Pilihlah salah satu: "))
a = int(input("Masukkan Masa Kerja Yang Ingin Ditentukan: "))
b = 1000000

if (pilih == "1") :
    if (a <= 5 ) :
        gaji = 2500000
    elif (a >= 6 > 10) :
        gaji = 3000000
    else :
        gaji = 3500000
elif (pilih == "2") :
    if (a <= 5) :
        gaji = 750000
    else :
        gaji = 1000000
else:
    print("Tidak ada gaji")
    
if (pilih == "1") :
    uang = 5000000
elif (pilih == "2") :
    uang = 2000000
else:
    print("Tidak ada tambahan")

print("Gaji total",  gaji+uang+b)