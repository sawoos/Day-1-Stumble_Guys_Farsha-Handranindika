nama = ["tono", "teddy", "wowo"]

# input
cari_nama = input("Masukkan nama yang ingin dicari posisinya: ")

if cari_nama in nama:
    posisi = nama.index(cari_nama)
    print(f"Ada woi, nama '{cari_nama}' di indeks ke-{posisi}.\n")
else:
    print(f"Sorri ye, nama si '{cari_nama}' tidak ada di daftar.\n")

# insert
nama_baru = input("Masukkan nama baru yang ingin ditambahkan: ")
nama.insert(1, nama_baru)

print("List terbaru:", nama)

# indeks
posisi_baru = nama.index(nama_baru)
print(f"'{nama_baru}' berhasil dimasukkan pada indeks ke-{posisi_baru}")