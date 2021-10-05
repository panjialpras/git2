import datetime
import os

x = datetime.datetime.now ()

def clear () :
    os.system ("cls")

booking_pertama = [{"nama" : str(input("Masukkan nama : ")),
                        "lama" : int(input("Masukkan lama waktu booking : ")),
                        "tgl" : int(input("Masukkan tanggal berapa penyewaan : ")),
                        "jam" : int(input("Jam berapa mulainya? ")),
                        "menit" : int(input("Masukkan menit ke berapa? "))}]

booking_selanjutnya = (booking_pertama).append

def tambah () :
    pili = input("Tambah data lagi? y/n : ")

    if pili == "y":
        while tambah == booking_pertama :
            print("Maaf data yang dimasukkan tidak dapat dimasukkan lagi")
            menu()

        else:
            print(booking_pertama)
            menu()
        #print[{"nama" : str(input("Masukkan nama : ")),
        #    "lama" : int(input("Masukkan lama waktu booking : ")),
        #    "tgl" : int(input("Masukkan tanggal berapa penyewaan : ")),
        #    "jam" : int(input("Jam berapa mulainya? ")),
        #    "menit" : int(input("Masukkan menit ke berapa? "))}].append
            
        #menu()

    else:
        menu()

def lihat_bookingan (booking_pertama) :
    print(["nama" == "Nama : ", 
    "billing" ==  "Lama Waktu : ", 
    "tgl" == "Tanggal : ", (x.strftime("%d")),
    "jam" == "Jam Mulai : ", (x.strftime("%H")),
    "menit" == "Menit : ", (x.strftime("%M"))
    (x.strftime("%p"))])
    #ada = 0
    #for a in booking_pertama :
        #if (a("bookingan_pertama") == booking_pertama) :
           # ada = 1
           # print("=" * 30)
           # print("=================")
           # print("Nama         :", a[nama])
           # print("Lama sewa    :", a[lama])
            #print("Tanggal      :", a[tgl])
            #print("Jam Mulai    :", a[jamul])
            #print("Menit        :", a[menit])
            #print("=" * 30)

            #return booking_pertama

            #break
    #if (ada == 0) :
        #print("Data booking tidak ada")


def hapus_booking (booking_pertama) :
    ketemu = 0
    for a in booking_pertama :
        if(a["hapus"] == booking_pertama) :

            ketemu == 1

            booking_pertama.remove
            print("Data telah dihapus")
        menu()

        break
    if (ketemu == 0):
        print("Data booking tidak ada")



def menu () :
    clear()
    print("-------------------------------")
    print("1. Tambah Data Penyewaan ")
    print("2. Cek Data Penyewaan ")
    print("3. Hapus Data Penyewaan ")
    print("4. Keluar ")
    print("-------------------------------")

    pilih = int(input("Masukkan menu pilihan anda : "))

    if pilih == 1 :
        tambah ()
    elif pilih == 2 :
        print(lihat_bookingan)
    elif pilih == 3 :
        hapus = input("Masukkan nama penyewa : ")
        hapus_booking(hapus)
    else:
        print("Anda telah keluar")
menu ()