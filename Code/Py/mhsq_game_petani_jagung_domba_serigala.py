#================================================================================
#Program Petani-Domba-Jagung-Serigala
#Pemain harus memindahkan petani, domba, jagung, dan serigala ke seberang sungai 
#menggunakan perahu yang hanya dapat memuat petani dan satu bawaan
#================================================================================
#import library
import os

#sub program (prosedur dan fungsi)
def tampil_gambar(list_kiri, list_kanan):
    print(list_kiri,"\____/,,,,,,,,,,",list_kanan)
    print("=======",                  "=========")

def menyeberang(list_kiri, list_kanan):

    pilih = "(P,J,D,S)"
    masuk = int(input("Seberangkan P,J,D,S"))

    while pilih != "D" :
        if pilih == "J" :
            print("Waduh, kamu gagal serigala memakan habis domba")
            main_lagi()
        elif pilih == "S":
            print("Waduh, kamu gagal Domba memakan habis jagung")
            main_lagi()
        else :
             print("Waduh, kamu gagal Domba memakan habis jagung")
             main_lagi()
    else:
        print(list_kiri.remove(D,P),",,,,,,,,\____/",list_kanan.append(D, P))
        print("=======",                  "=========")
        if pilih == "P":
            print(list_kiri.append(P),"\____/,,,,,,,",list_kanan.remove(P))
            print("=======",                           "=======")
        else :
            print("Yang ingin anda pindahkan, bersebrangan dengan P")
            if pilih == "S":
                print(list_kiri.remove(P,S),",,,,,,,\____/",list_kanan.append(P.S))
            elif pilih == "J":
                tampil_gambar(list_kiri.remove(P,J),",,,,,,,\_____/",list_kanan.append(P,J))

def cek_selesai(list_kiri, list_kanan):
    print("silakan isi kode program untuk prosedur tampil_gambar()")

#program utama
os.system("cls")
list_kiri = ['P', 'J', 'D', 'S']
list_kanan = []
selesai = False     #False jika permainan belum berakhir. True jika permainan berakhir
main_lagi = 'Y'     #'Y' jika user ingin bermain lagi. 'T' jika user tidak ingin bermain lagi

tampil_gambar(list_kiri, list_kanan)

while (main_lagi.upper() == 'Y'):
    menyeberang(list_kiri, list_kanan)

    os.system("cls")
    tampil_gambar(list_kiri, list_kanan)

    selesai = cek_selesai(list_kiri, list_kanan)

    #jika selesai = True, tanya apakah mau main lagi atau tidak
    if (selesai):
        main_lagi = input("\nMain lagi (Y/T)? ")

        #jika main_lagi = 'Y', reset lagi list_kiri dan list_kanan
        os.system("cls")
        list_kiri = ['P', 'J', 'D', 'S']
        list_kanan = []
        tampil_gambar(list_kiri, list_kanan)
    

# Panji Al Muqsith Prasetyo
# 5200411249