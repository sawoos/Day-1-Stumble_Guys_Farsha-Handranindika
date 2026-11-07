
#3  temp % 10 mengambil digit paling kanan (sisa bagi 10).



#4 Perulangan berjalan maksimal 3 kali. Jika input cocok dengan PASSWORD_BENAR, perintah break menghentikan loop. 
# Jika gagal 3 kali, pesan "Akun terkunci" akan ditampilkan.
PASSWORD_BENAR = "python123"
percobaan = 0
max_percobaan = 3

while percobaan < max_percobaan:
    pw = input("Masukkan password: ")
    if pw == PASSWORD_BENAR:
        print("Login berhasil")
        break
    percobaan += 1
    if percobaan < max_percobaan:
        print(f"Password salah. Sisa percobaan: {max_percobaan - percobaan}")

if percobaan == max_percobaan and pw != PASSWORD_BENAR:
    print("Akun terkunci")

#5 while True membuat perulangan tak terbatas yang hanya berhenti jika pengguna memasukkan angka 0. 
# Setelah keluar dari perulangan, program menghitung rata-rata dengan membagi total dengan jumlah_data.
total = 0
jumlah_data = 0

while True:
    angka = float(input("Masukkan angka (0 untuk berhenti): "))
    if angka == 0:
        break
    total += angka
    jumlah_data += 1

if jumlah_data > 0:
    rata_rata = total / jumlah_data
    print(f"Jumlah total: {total}")
    print(f"Rata-rata: {rata_rata:.2f}")
else:
    print("Tidak ada angka yang dimasukkan.")

#6 Loop luar mencetak baris sebanyak n kali, sedangkan loop 
# dalam mencetak karakter * sebanyak n kali secara mendatar pada setiap baris.
n = int(input("Masukkan ukuran persegi (n): "))

for i in range(n):
    for j in range(n):
        print("*", end=" ")
    print()

#7 Loop i menentukan angka pengali pertama (baris), dan loop j menentukan pengali kedua (kolom). 
# Format :4d digunakan agar lebar tampilan angka sejajar rapi.
print("=== TABEL PERKALIAN 1 - 10 ===\n")
for i in range(1, 11):
    for j in range(1, 11):
        print(f"{i * j:4d}", end="")
    print()

#8 Loop luar i menentukan nomor baris (1 hingga 5). 
# Loop dalam j mencetak angka mulai dari 1 hingga nilai i pada baris tersebut.
for i in range(1, 6):
    for j in range(1, i + 1):
        print(j, end=" ")
    print()

#9 Loop luar mengontrol 4 baris, sedangkan loop dalam mengontrol 5 kolom untuk menampilkan koordinat
for baris in range(1, 5):
    for kolom in range(1, 6):
        print(f"({baris},{kolom})", end=" ")
    print()

#10 Menghasilkan seluruh kombinasi pasangan (i, j) di mana variabel i 
# beriterasi dari 1 sampai 5 dan variabel j beriterasi dari 1 sampai 5.
for i in range(1, 6):
    for j in range(1, 6):
        print(f"({i}, {j})", end=" ")
    print()