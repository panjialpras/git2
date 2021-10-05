# Panji Al Muqsith Prasetyo
# 5200411249
#program pendataan mahasiswa
#---------------------------
#library
import os

#sub program
def tambah_data_mhs():
    input_nim     = int(input("NIM\t\t: "))
    input_nama    = input("Nama Lengkap\t: ")
    input_gender  = input("Gender (L/P)\t: ")
    input_prodi   = input("Program Studi\t: ")
    input_ipk     = float(input("IPK\t\t: "))

    #mengisi data ke dictionary
    data_mhs = {"nim": input_nim, 
                "nama": input_nama, 
                "gender": input_gender, 
                "prodi": input_prodi, 
                "ipk": input_ipk}

    #memasukkan data dictionary ke dalam list
    data_semua_mhs.append(data_mhs)

def tampil_data_mhs():
    if (len(data_semua_mhs) == 0):
        print("Data mahasiswa masih kosong")
    else:
        print("NIM \t Nama Mahasiswa \t Gender  Program Studi \t IPK")
        print("----\t----------------\t-------  --------------\t-----")
        
        #menampilkan satu per satu dictionary data_mhs di dalam list data_semua_mhs
        for mhs in data_semua_mhs:
            print(mhs["nim"], "\t", mhs["nama"], "\t\t\t", mhs["gender"], "\t", mhs["prodi"], "\t", mhs["ipk"])

def hapus_data_mhs(nim):
    for mhs in range (len(data_semua_mhs)) :
        if hapus == data_semua_mhs[mhs]["nim"] :
            data_semua_mhs.pop(mhs)
            print("data berhasil dihapus")

def cari_data_mhs(nim):
    for mhs in data_semua_mhs :
        if mhs["nim"] == cari :
            print("NIM \t Nama Mahasiswa \t Gender  Program Studi \t IPK")
            print("----\t----------------\t-------  --------------\t-----")
            print(mhs["nim"], "\t", mhs["nama"], "\t\t\t", mhs["gender"], "\t", mhs["prodi"], "\t", mhs["ipk"])
        else :
            print("Maaf NIM tidak ada")
#program utama
#inisialisasi variabel global (variabel yang bisa diakses lewat manapun)
data_mhs = {}       #dictionary
data_semua_mhs = [] #list
menu = 0

while (menu != 5):
    #membersihkan layar command prompt
    os.system("cls")

    #menampilkan menu
    print("----------------------------")
    print("Aplikasi Pendataan Mahasiswa UTY")
    print("1. Lihat Data Mahasiswa")
    print("2. Tambah Data Mahasiswa")
    print("3. Hapus Data Mahasiswa")
    print("4. Cari Data Mahasiswa")
    print("5. Keluar")
    print("----------------------------")
    menu = int(input("Pilih Menu: "))

    #cek menu
    if (menu == 1):
        tampil_data_mhs()
    elif (menu == 2):
        tambah_data_mhs()
    elif (menu == 3):
        hapus = input("Masukkan NIM yang akan dihapus: ")
        hapus_data_mhs(hapus)
    elif (menu == 4):
        cari = input("Masukkan NIM yang ingin dicari: ")
        cari_data_mhs(cari)
    elif (menu == 5):
        print("Anda telah keluar")
    else:
        print("Menu yang dipilih tidak tersedia")
    
    #menunggu user menekan enter untuk melanjutkan
    input("\nTekan ENTER untuk melanjutkan")