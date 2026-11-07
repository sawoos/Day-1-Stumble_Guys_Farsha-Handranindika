# 1 Aplikasi Quiz 

# Data soal kuis menggunakan list of dictionary
soal_quiz = [
    {
        "pertanyaan": "1. Apa ibu kota negara Indonesia?",
        "pilihan": ["A. Surabaya", "B. Jakarta", "C. Bandung", "D. Medan"],
        "jawaban": "B"
    },
    {
        "pertanyaan": "2. Berapakah hasil dari 5 dikali 5?",
        "pilihan": ["A. 10", "B. 20", "C. 25", "D. 30"],
        "jawaban": "C"
    },
    {
        "pertanyaan": "3. Warna bendera negara Indonesia adalah?",
        "pilihan": ["A. Merah Putih", "B. Biru Putih", "C. Merah Kuning", "D. Hijau Putih"],
        "jawaban": "A"
    }
]

# While loop utama untuk menjaga program tetap berjalan (Minimal 1 while loop)
while True:
    print("\n=== APLIKASI QUIZ PENGETAHUAN UMUM ===")
    print("1. Mulai Quiz")
    print("2. Lihat Panduan")
    print("3. Keluar")
    
    # Error handling dasar untuk input menu
    try:
        pilihan_menu = int(input("Pilih menu (1-3): "))
    except ValueError:
        print("Error: Input harus berupa angka!")
        continue

    if pilihan_menu == 1:
        skor = 0
        
        # Nested loop: For loop untuk soal + For loop untuk opsi + While loop untuk validasi
        for item in soal_quiz:
            print("\n" + item["pertanyaan"])
            for opt in item["pilihan"]:
                print(opt)
            
            # Inner while loop untuk validasi input jawaban
            while True:
                jawaban_user = input("Pilih jawaban (A/B/C/D): ").strip().upper()
                
                # Validasi input: memastikan pilihan hanya A, B, C, atau D
                if jawaban_user in ['A', 'B', 'C', 'D']:
                    break # Keluar dari loop validasi jika input benar
                print("Error: Harap masukkan pilihan A, B, C, atau D!")
            
            # Cek jawaban
            if jawaban_user == item["jawaban"]:
                print("-> Jawaban BENAR!")
                skor += 1
            else:
                print(f"-> Jawaban SALAH! Jawaban yang benar adalah {item['jawaban']}.")
        
        print(f"\nQuiz Selesai! Skor Akhir Anda: {skor}/{len(soal_quiz)}")
        
    elif pilihan_menu == 2:
        print("\n--- PANDUAN QUIZ ---")
        print("1. Jawab pertanyaan dengan memilih opsi A, B, C, atau D.")
        print("2. Setiap jawaban benar mendapatkan 1 poin.")
        
    elif pilihan_menu == 3:
        print("Terima kasih telah bermain!")
        break # Penggunaan break untuk keluar dari program
        
    else:
        print("Error: Pilihan menu tidak valid!")


# 2 Sistem Inventori Barang Toko Sederhana

inventori = [
    ["Buku Tulis", "Alat Tulis", 10],
    ["Roti Tawar", "Makanan", 5],
    ["Air Mineral", "Minuman", 12]
]

# While loop utama (Minimal 1 while loop)
while True:
    print("\n=== SISTEM INVENTORI BARANG TOKO ===")
    print("1. Lihat Daftar Barang")
    print("2. Tambah Barang Baru")
    print("3. Keluar")
    
    # Error handling dasar
    try:
        pilihan = int(input("Pilih menu (1-3): "))
    except ValueError:
        print("Error: Input menu harus berupa angka!")
        continue

    if pilihan == 1:
        print("\n--- DAFTAR BARANG PER KATEGORI ---")
        daftar_kategori = ["Alat Tulis", "Makanan", "Minuman"]
        
        # Nested loop: Loop kategori (outer) dan loop data inventori (inner)
        for kat in daftar_kategori:
            print(f"\n[ Kategori: {kat} ]")
            ada = False
            for item in inventori:
                if item[1] == kat:
                    print(f"- {item[0]} | Stok: {item[2]} unit")
                    ada = True
            if not ada:
                print("- (Belum ada barang)")

    elif pilihan == 2:
        print("\n--- TAMBAH BARANG BARU ---")
        
        # Validasi nama barang tidak boleh kosong
        while True:
            nama = input("Masukkan nama barang: ").strip()
            if nama != "":
                break
            print("Error: Nama barang tidak boleh kosong!")

        # Validasi pilihan kategori
        while True:
            print("Pilih Kategori: 1. Alat Tulis | 2. Makanan | 3. Minuman")
            kat_input = input("Masukkan pilihan (1-3): ").strip()
            if kat_input == "1":
                kategori = "Alat Tulis"
                break
            elif kat_input == "2":
                kategori = "Makanan"
                break
            elif kat_input == "3":
                kategori = "Minuman"
                break
            print("Error: Pilihan kategori salah!")

        # Validasi jumlah stok harus angka positif
        while True:
            try:
                jumlah = int(input("Masukkan jumlah stok: "))
                if jumlah > 0:
                    break # Keluar dari loop jika input valid
                print("Error: Stok harus lebih dari 0!")
            except ValueError:
                print("Error: Stok harus berupa angka bulat!")

        # Menambahkan barang ke daftar
        inventori.append([nama, kategori, jumlah])
        print(f"Berhasil menambahkan '{nama}' ke inventori!")

    elif pilihan == 3:
        print("Keluar dari sistem inventori... Terima kasih!")
        break # Menghentikan perulangan utama

    else:
        print("Error: Pilihan menu tidak ada!")