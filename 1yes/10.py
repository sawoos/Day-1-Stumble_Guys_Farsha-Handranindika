def text_analyzer():
    teks = ""
    while True:
        print("             TEXT ANALYZER               ")
        print("========================================")
        if teks:
            print(f"Teks saat ini : '{teks}'")
        else:
            print("Teks saat ini : (Belum ada teks)")
        print("----------------------------------------")
        print("1. Masukkan / Ubah Teks")
        print("2. Ubah Teks ke Huruf Besar (Uppercase)")
        print("3. Ubah Teks ke Huruf Kecil (Lowercase)")
        print("4. Hitung Jumlah Karakter (Total & Tanpa Spasi)")
        print("5. Hitung Jumlah Kata")
        print("6. Hitung Vokal dan Konsonan")
        print("7. Balik Teks (Menggunakan Slicing)")
        print("8. Cek Palindrom")
        print("9. Keluar")
        print("----------------------------------------")
        
        pilihan = input("Pilih menu (1-9): ").strip()
        
        # Validasi input menu harus berupa angka
        if not pilihan.isdigit():
            print("\n[ERROR] Pilihan tidak valid! Harap masukkan angka 1-9.")
            continue
            
        pilihan = int(pilihan)
        
        if pilihan == 1:
            teks = input("Masukkan teks baru: ")
            print("-> Teks berhasil disimpan!")
            
        elif pilihan == 9:
            print("\nKeluar dari program. Terima kasih!")
            break
            
        else:
            # Validasi jika user belum memasukkan teks tapi memilih menu analitik
            if not teks:
                print("\n[PERINGATAN] Harap masukkan teks terlebih dahulu melalui Menu 1!")
                continue
                
            if pilihan == 2:
                print(f"Hasil Uppercase: {teks.upper()}")
                
            elif pilihan == 3:
                print(f"Hasil Lowercode: {teks.lower()}")
                
            elif pilihan == 4:
                total_karakter = len(teks)
                tanpa_spasi = len(teks.replace(" ", ""))
                print(f"Jumlah total karakter (dengan spasi): {total_karakter}")
                print(f"Jumlah karakter (tanpa spasi): {tanpa_spasi}")
                
            elif pilihan == 5:
                kata = teks.split()
                print(f"Jumlah kata: {len(kata)}")
                
            elif pilihan == 6:
                vokal_set = "aiueoAIUEO"
                jml_vokal = 0
                jml_konsonan = 0
                for char in teks:
                    if char.isalpha(): # Menggunakan loop untuk analisis karakter
                        if char in vokal_set:
                            jml_vokal += 1
                        else:
                            jml_konsonan += 1
                print(f"Jumlah huruf vokal: {jml_vokal}")
                print(f"Jumlah huruf konsonan: {jml_konsonan}")
                
            elif pilihan == 7:
                # Menggunakan Slicing
                teks_terbalik = teks[::-1]
                print(f"Teks setelah dibalik: {teks_terbalik}")
                
            elif pilihan == 8:
                # Cek palindrom (mengabaikan spasi dan huruf besar/kecil)
                bersih = teks.lower().replace(" ", "")
                if bersih == bersih[::-1]:
                    print(f"'{teks}' adalah PALINDROM.")
                else:
                    print(f"'{teks}' BUKAN palindrom.")
                    
            else:
                print("\n[ERROR] Pilihan menu tidak tersedia. Silakan pilih 1-9.")

if __name__ == "__main__":
    text_analyzer()