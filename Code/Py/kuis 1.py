# Panji Al Muqsith Prasetyo
# 5200411249

menu = [["Baju", 120000], ["Kaos", 80000], ["Celana pendek", 100000], ["Celana Panjang", 150000], ["Jaket", 250000],["Rok",60000]]

def daftar_barang():
    print(" No | Nama Barang         | Harga          ")
    i = 1
    for item in menu:
        print(" " + str(i) + "  |" + item[0] + "                 | " + str(item[1]) + " ")
        i += 1
    print(" selesai | Checkout ")
    return


daftar_barang()
jawaban = ""
catatan_pilihan = []
while jawaban != "selesai":
    jawaban = input("Pilih Nama Barang: ") 
    daftar_barang()
    if jawaban != "selesai":
        catatan_pilihan.append(int(jawaban)-1)

no = 1
print("Barang : ")
total = 0
for pilihan in catatan_pilihan:
    print("barang ke-" + str(no) + " = " + menu[pilihan][0] + " Harga + " + str(menu[pilihan][1]))
    no += 1
    total  = total + menu[pilihan][1]

print("Total pembayaran Rp. " + str(total))

print("                    ")
print("Menentukan Harga Diskon") 
print("Kartu Member\n1. platinum\n2. gold\n3. silver\n")
i=str(input("masukan kartu pelanggan: "))
if(i == 'platinum'):
    harga=int(input("Total pembayaran Rp. "))
    if (harga>=0):
        harga_diskon=harga*0.1
        diskon = harga - harga_diskon
    print (diskon)
elif(i == 'gold'):
    harga=int(input("Total pembayaran Rp. "))
    if (harga>=300000):
        harga_diskon=harga*0.1
        diskon = harga - harga_diskon
    print (diskon)
elif(i == 'silver'):
    harga=int(input("Total pembayaran Rp. "))
    if (harga>=250000):
        harga_diskon=harga-50000
        diskon = harga - harga_diskon
    print (diskon)
else:
    harga=int(input("Total pembayaran Rp."))
    print("total pembayaran Rp.",harga)