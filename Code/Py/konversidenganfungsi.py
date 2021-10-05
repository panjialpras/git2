print("=========== konversi mata uang ==========")
print("1. Rupiah ke Euro\n2.Euro ke Rupiah")

ulang = True
while(ulang == True):
    pilihan = int(input("masukan pilihan: "))
    if(pilihan == 1):
        nominal = int(input("masukan nominal Rupiah: Rp."))
        hasil = str(nominal / 15000)[0:4]
        print("€",hasil)
        break
    elif(pilihan == 2):
        nominal = int(input("masukan nominal Euro: "))
        hasil = nominal * 15000
        print("Rp.",hasil)
        break
    else:
        print("\npilihan tidak ada")

