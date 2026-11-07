def tampilkan_data(**kwargs):
    for kunci, nilai in kwargs.items():
        print(f"{kunci}: {nilai}")

tampilkan_data(nama="Nina", prodi="informatika", semester=3)