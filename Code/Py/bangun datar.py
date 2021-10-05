print("Pilihlah bangun datar yang akan dihitung")

print ("1.Persegi")
print ("2.Persegi Panjang")
print ("3.Segitiga")
print ("4.Lingkaran")
pilihan = int(input("Masukkan Pilihan Anda: "))

if (pilihan == 1):
    sisi = int(input("Masukkan sisi yang anda inginkan: "))
    luas = sisi*sisi
    print("Luas Persegi: ",luas)
elif (pilihan == 2):
    panjang = int(input("Masukkan Panjang yang anda inginkan: "))
    lebar = int(input("Masukkan lebar yang anda inginkan: "))
    keliling = panjang*lebar
    print("Luas Persegi Panjang: ",luas)
elif (pilihan == 3):
    alas = int(input("Masukkan Alas yang anda ingikan: "))
    tinggi = int(input("Masukkan tinggi yang anda inginkan: "))
    luas = 1/2*alas*tinggi
    print("Luas Segitiga: ",luas)
elif (pilihan == 4):
    r = int(input("Masukkan jari-jari yang anda inginkan: "))
    luas = 22/7*r*r
    print("Luas lingkaran: ",luas)
else :
    print("Coba liat lagi pilihannya apa saja ya~")