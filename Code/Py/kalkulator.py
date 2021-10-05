angka_1 = int(input("input angka pertama: "))
operator = input("Input operator: ")
angka_2 = int(input("input angka kedua: "))

if (operator == "+") :
    hasil = angka_1 + angka_2
elif (operator == "-") :
    hasil = angka_1 - angka_2
elif (operator == "*") :
    hasil = angka_1 * angka_2
elif (operator == "/") :
    hasil = angka_1 / angka_2
elif (operator == "//") :
    hasil = angka_1 // angka_2
elif (operator == "**") :
    hasil = angka_1 ** angka_2
elif (operator == "%") :
    hasil = angka_1 % angka_2

print (hasil)