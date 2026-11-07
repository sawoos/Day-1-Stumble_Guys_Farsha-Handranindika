# 4
teks = input("Masukkan teks: ")
karakter_ganjil = teks[1::2]

print("Karakter pada indeks ganjil:", karakter_ganjil)

# 5
teks = input("Masukkan teks: ")
teks_terbalik = teks[::-1]

print("di balik", teks_terbalik)

# 6
teks = input("Masukkan teks utama: ")
substring = input("Masukkan substring yang dicari: ")

if substring in teks:
    print(f"Substring '{substring}' ditemukan dalam teks.")
else:
    print(f"Substring '{substring}' tidak ditemukan dalam teks.")