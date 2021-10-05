#Kasus > Flowchart > Coding
# Boolean = True False
# string (str) kalimat
# int = bilangan bulat
# float = bilangan desimal
# hexadesimal (hex) = format heksa
# jawab = 'ya'
# hitung = 0

# while(jawab == 'ya'):
#     print("Perulangan ke-",hitung)
#     hitung = hitung+1
#     jawab = input("Ulang lagi ? ")
# else:
#     print ("Total Perulangan : ", hitung)

#contoh perulangan for dan if
import mysql.connector

db = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd=""
)

if db.is_connected():
  print("Berhasil terhubung ke database")
