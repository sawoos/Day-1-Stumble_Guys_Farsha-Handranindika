"""
Program Integrasi Praktikum Algoritma dan Pemrograman
Fitur: Faktorial, Fibonacci, Perpangkatan Cepat, dan Pemrosesan Daftar Nilai
"""

import sys

# 1. FUNGSI FAKTORIAL (Rekursif & Iteratif)
def faktorial_rekursif(n):
    """
    Menghitung n! secara rekursif.
    Base Case: n == 0 atau n == 1 -> mengembalikan 1
    Recursive Call: n * faktorial_rekursif(n - 1)
    """
    if n == 0 or n == 1:  # Base case
        return 1
    return n * faktorial_rekursif(n - 1)  # Recursive call

def faktorial_iteratif(n):
    """Menghitung n! secara iteratif menggunakan perulangan loop."""
    hasil = 1
    for i in range(2, n + 1):
        hasil *= i
    return hasil

def menu_faktorial():
    print("\n--- [1] KALKULATOR FAKTORIAL ---")
    try:
        n = int(input("Masukkan bilangan bulat non-negatif (n >= 0): "))
        if n < 0:
            print("Peringatan: Input tidak boleh bernilai negatif!")
            return
        
        res_rek = faktorial_rekursif(n)
        res_ite = faktorial_iteratif(n)
        
        print(f"Hasil Faktorial Rekursif ({n}!): {res_rek}")
        print(f"Hasil Faktorial Iteratif ({n}!): {res_ite}")
    except ValueError:
        print("Pesan Kesalahan: Input harus berupa angka bulat!")

# 2. FUNGSI FIBONACCI (Rekursif, Memoization, Iteratif)
def fibonacci_rekursif(n):
    """
    Base Case: n == 0 -> 0, n == 1 -> 1
    Recursive Call: fib(n-1) + fib(n-2)
    """
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    return fibonacci_rekursif(n - 1) + fibonacci_rekursif(n - 2)

def fibonacci_memoization(n, memo={}):
    """Fibonacci dengan Memoization untuk efisiensi kompleksitas waktu."""
    if n in memo:
        return memo[n]
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    memo[n] = fibonacci_memoization(n - 1, memo) + fibonacci_memoization(n - 2, memo)
    return memo[n]

def fibonacci_iteratif(n):
    """Fibonacci iteratif O(n) waktu, O(1) memori."""
    if n <= 0:
        return 0
    if n == 1:
        return 1
    a, b = 0, 1
    for _ in range(2, n + 1):
        a, b = b, a + b
    return b

def menu_fibonacci():
    print("\n--- [2] DERET FIBONACCI ---")
    try:
        n = int(input("Masukkan suku ke-n (n >= 0): "))
        if n < 0:
            print("Peringatan: Posisi deret tidak boleh negatif!")
            return
            
        print(f"Fibonacci Iteratif (Suku ke-{n}): {fibonacci_iteratif(n)}")
        print(f"Fibonacci Memoization (Suku ke-{n}): {fibonacci_memoization(n)}")
        if n <= 30: # Batasi naif agar komputer tidak hang saat testing
            print(f"Fibonacci Rekursif Naif (Suku ke-{n}): {fibonacci_rekursif(n)}")
        else:
            print("Fibonacci Rekursif Naif dilewati untuk efisiensi (n > 30).")
    except ValueError:
        print("Pesan Kesalahan: Input harus berupa angka bulat!")


# 3. FUNGSI PERPANGKATAN CEPAT (Fast Exponentiation)
def pangkat_cepat(a, b):
    """
    Menghitung a^b menggunakan pendekatan Divide and Conquer O(log b).
    Base Case: b == 0 -> 1
    Recursive Call: 
      - Jika b genap : pangkat_cepat(a, b//2)^2
      - Jika b ganjil: a * pangkat_cepat(a, b-1)
    """
    if b == 0:  # Base case
        return 1
    if b % 2 == 0:
        setengah = pangkat_cepat(a, b // 2)
        return setengah * setengah
    else:
        return a * pangkat_cepat(a, b - 1)

def menu_perpangkatan():
    print("\n--- [3] PERPANGKATAN CEPAT (a^b) ---")
    try:
        a = float(input("Masukkan basis (a): "))
        b = int(input("Masukkan eksponen/pangkat non-negatif (b >= 0): "))
        if b < 0:
            print("Peringatan: Pangkat harus berupa bilangan non-negatif!")
            return
        
        hasil = pangkat_cepat(a, b)
        print(f"Hasil dari {a}^{b} adalah: {hasil}")
    except ValueError:
        print("Pesan Kesalahan: Format angka tidak valid!")

# 4. PROSES DAFTAR NILAI (Functional Programming Tools)
def menu_daftar_nilai():
    print("\n--- [4] PROSES DAFTAR NILAI SISWA ---")
    raw_input = input("Masukkan daftar nilai dipisahkan spasi (contoh: 85 60 75 90 55): ")
    try:
        nilai_list = [float(x) for x in raw_input.split()]
        if not nilai_list:
            print("Peringatan: Daftar nilai tidak boleh kosong!")
            return
        
        # 1. Filter nilai >= 70
        nilai_lulus = list(filter(lambda x: x >= 70, nilai_list))
        
        # 2. Sorted dari tertinggi ke terendah
        nilai_terurut = sorted(nilai_list, key=lambda x: x, reverse=True)
        
        # 3. Map label "Lulus" atau "Belum"
        label_status = list(map(lambda x: (x, "Lulus" if x >= 70 else "Belum"), nilai_list))
        
        print("\n>>> HASIL PEMROSESAN DATA NILAI <<<")
        print(f"1. Semua Nilai Input : {nilai_list}")
        print(f"2. Nilai Terurut (Ascending/Descending): {nilai_terurut}")
        print(f"3. Filter Nilai Lulus (>= 70)          : {nilai_lulus}")
        print("4. Label Status Kelulusan:")
        for val, status in label_status:
            print(f"   - Nilai {val}: {status}")
            
    except ValueError:
        print("Pesan Kesalahan: Pastikan seluruh nilai diinput dalam bentuk angka!")

# MENU UTAMA
def main():
    while True:
        print("\n===== MENU PRAKTIKUM =====")
        print("1. Faktorial")
        print("2. Fibonacci")
        print("3. Perpangkatan cepat")
        print("4. Proses daftar nilai")
        print("0. Keluar")
        pilihan = input("Pilih menu (0-4): ").strip()

        if pilihan == "1":
            menu_faktorial()
        elif pilihan == "2":
            menu_fibonacci()
        elif pilihan == "3":
            menu_perpangkatan()
        elif pilihan == "4":
            menu_daftar_nilai()
        elif pilihan == "0":
            print("Program selesai. Terima kasih!")
            break
        else:
            print("Pilihan menu tidak valid. Masukkan angka 0, 1, 2, 3, atau 4.")

if __name__ == "__main__":
    main()  