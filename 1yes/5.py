#1
angka = 2
while angka <= 20:     
    print(angka)     
    angka += 2

#2
angka =int(input("Masukkan angka awal countdown: "))
while angka >= 1:
    print(angka)
    angka -= 1
print("GO!")

#3
nilai = int(input("Masukkan nilai 0-100: "))
while nilai < 0 or nilai > 100:
    print("Nilai tidak valid.")
    nilai = int(input("Masukkan nilai 0-100: "))
print("Nilai diterima:", nilai)

#4
while True:
    print("\n=== MENU ===")
    print("1. Halo")
    print("2. Informasi")
    print("3. Keluar")
    
    pilihan = input("Pilih menu: ")
    
    if pilihan == "1":
        print("Halo, selamat belajar Python!")
    elif pilihan == "2":
        print("Anda sedang mempelajari while loop.")
    elif pilihan == "3":
        print("Program selesai.")
        break
    else:
        print("Pilihan tidak tersedia.")

#5
for i in range(5, 0, -1):
    for j in range(i):
        print("*", end=" ")
    print()