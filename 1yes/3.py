penghasilan = float(input("Masukkan penghasilan orang tua/tahun (Rp): "))
listrik = float(input("Masukkan daya meteran listrik (VA/Volts): "))
jumlah_mobil = int(input("Masukkan jumlah mobil yang dimiliki: "))

mobil_diatas_2000 = False
if jumlah_mobil > 0:
    tahun_mobil = int(input("Masukkan tahun pembuatan mobil terbaru: "))
    if tahun_mobil > 2000:
        mobil_diatas_2000 = True

jumlah_motor = int(input("Masukkan jumlah motor yang dimiliki: "))

alasan_penolakan = []

if penghasilan > 100000000:
    alasan_penolakan.append("Penghasilan orang tua melebihi Rp 100 juta/tahun")

if listrik > 2200:
    alasan_penolakan.append("Daya listrik melebihi 2200 VA/Volts")

if mobil_diatas_2000:
    alasan_penolakan.append("Memiliki mobil keluaran di atas tahun 2000")

if jumlah_motor > 1:
    alasan_penolakan.append("Memiliki motor lebih dari 1 unit")

print("\n" + "-" * 40)
if len(alasan_penolakan) == 0:
    print("STATUS: ELIGIBLE (Lolos Beasiswa)")
else:
    print("STATUS: TIDAK ELIGIBLE")
    for alasan in alasan_penolakan:
        print(f"- {alasan}")
print("-" * 40)