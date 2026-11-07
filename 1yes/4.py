#Latihan 5.1
#No.1
teks_1 = "ALGORITHM"
for karakter in teks_1 :
    print(karakter)

#No.2
teks_2 = input("Masukan Kalimat/String: ")
jumlah_a = teks_2.lower().count("a")
print(f"huruf 'a' Atau 'A' muncul sebanyak: {jumlah_a} kali")

#No.3
teks_3 = input("Hitung Karakter String dari:  ")
panjang_string = len(teks_3)
print(f"Jumlah total karakter: {panjang_string}")

#No.4
teks_4 = input("Masukan Teks: ")
jumlah_I_besar = teks_4.count("I")
jumlah_i_kecil = teks_4.count("i")
total_i = jumlah_I_besar + jumlah_i_kecil

print(f"Jumlah huruf 'T' (kapital):  {jumlah_I_besar}")
print(f"Jumlah huruf 't' (kecil):  {jumlah_i_kecil}")
print(f"Total huruf 'T' dan 't' : {total_i}")


#Latihan 8.2
#No. 1
def faktorial(n):
    hasil = 1
    for i in range(1, n + 1):
        hasil *= i
    return hasil

print("5! =", faktorial(5))
print("7! =", faktorial(7))
print("10! =", faktorial(10)) 

#No. 2 dan 3
n = int(input("Masukkan angka: "))

if n < 0:
    print("Error BOSKU: Faktorial tidak didefinisikan untuk bilangan negatif.")
else:
    hasil = 1
    for i in range(1, n + 1):
        hasil *= i
    print(f"Hasil {n}! = {hasil}")