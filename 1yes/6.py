import time

def main():
    while True:
        print("--------------------------------------------------")
        print("         SISTEM ANALISIS NILAI MAHASISWA         ")
        print("--------------------------------------------------")
        
        # Input Jumlah Mahasiswa (N > 0)
        N = int(input("Jumlah mahasiswa: "))
        while N <= 0:
            print("Error: Jumlah mahasiswa harus lebih dari 0!")
            N = int(input("Jumlah mahasiswa: "))
            
        print("-" * 50)
        
        # Inisialisasi Variabel (Accumulator, Counter, Tracking)
        total_nilai = 0.0          # Accumulator
        jumlah_lulus = 0           # Counter untuk nilai >= 60
        jumlah_sangat_baik = 0     # Counter untuk nilai >= 80 
        
        nilai_maksimum = None       # Peracak nilai maksimum
        nilai_minimum = None       # Peracak nilai minimum 
        
        # Mulai mengukur waktu eksekusi 
        waktu_mulai = time.perf_counter()
        
        # Loop Utama
        for i in range(1, N + 1):
            nilai = float(input(f"Nilai {i}: "))
            
            # Kategori nilai 
            if nilai >= 85:
                kategori = "A (Sangat Baik)"
            elif nilai >= 75:
                kategori = "B (Baik)"
            elif nilai >= 60:
                kategori = "C (Cukup)"
            elif nilai >= 50:
                kategori = "D (Kurang)"
            else:
                kategori = "E (Gagal)"
                
            print(f"   -> Kategori: {kategori}")
            
            # Akumulasi Total
            total_nilai += nilai
            
            # Penghitungan Jumlah Lulus dan Nilai >= 80
            if nilai >= 60:
                jumlah_lulus += 1
            if nilai >= 80:
                jumlah_sangat_baik += 1
                
            # Nilai Maksimum & Minimum
            if nilai_maksimum is None or nilai > nilai_maksimum:
                nilai_maksimum = nilai
            if nilai_minimum is None or nilai < nilai_minimum:
                nilai_minimum = nilai

        # Selesai Loop - Menghentikan Waktu
        waktu_selesai = time.perf_counter()
        durasi = (waktu_selesai - waktu_mulai) * 1000  # Konversi ke milidetik

        # Rata-rata
        rata_rata = total_nilai / N

        # Hasil
        print("\n" + "=" * 50)
        print("                 HASIL ANALISIS                   ")
        print("-" * 50)
        print(f"Total nilai                 : {total_nilai:.2f}")
        print(f"Rata-rata                   : {rata_rata:.2f}")
        print(f"Jumlah lulus (>= 60)        : {jumlah_lulus}")
        print(f"Jumlah nilai >= 80          : {jumlah_sangat_baik}")
        print(f"Nilai maksimum              : {nilai_maksimum:.2f}")
        print(f"Nilai minimum               : {nilai_minimum:.2f}")
        print(f"Durasi proses input         : {durasi:.2f} ms")
        print("=" * 50)

        # Bisa di Ulangi
        ulang = input("\nApakah ingin menjalankan kembali pengolahan data? (y/n): ").strip().lower()
        if ulang != 'y':
            print("\nTerima kasih telah menggunakan Sistem Analisis Nilai Mahasiswa!")
            break
        print("\n")

if __name__ == "__main__":
    main()

#Farsha Handranindika_2607441021 (RKS 1B)