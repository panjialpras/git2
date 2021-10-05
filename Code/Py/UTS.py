bilangan = int(input("Masukkan Angka: "))

if (bilangan % 2 == 1):
    hasil = bilangan + 1
    print(hasil)
elif (bilangan == 21 ) | (bilangan == 27) :
    hasil = bilangan + 1
    print(hasil)
else:
    print(bilangan)

while bilangan != 100 :
    bilangan = int(input("Masukkan bilangan: "))
    print(bilangan)
else:
    print("Program telah selesai")