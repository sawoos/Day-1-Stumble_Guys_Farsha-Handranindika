"""
POTENSIAL LISTRIK INTERAKTIF (SymPy)
Rumus diturunkan dulu secara simbolik, lalu kamu memasukkan datanya.
Tetapan fisika (epsilon_0, k) sudah tetap, jadi tidak perlu diinput.
Semua input memakai satuan SI. Boleh pakai notasi ilmiah, contoh: 1e-9
"""

import sympy as sp

EPS0 = 8.854187817e-12   # F/m, tetap

# ---------- Simbol ----------
eps0 = sp.symbols("epsilon_0", positive=True)
k = 1 / (4 * sp.pi * eps0)
q, Q, a, R, L = sp.symbols("q Q a R L", positive=True)
r, z, y, d = sp.symbols("r z y d", positive=True)
sigma, lam = sp.symbols("sigma lambda", positive=True)


# ---------- Alat bantu ----------
def baca(teks, boleh_negatif=False):
    """Minta angka dari pengguna, ulangi sampai valid."""
    while True:
        s = input(f"  {teks} : ").strip().replace(",", ".")
        try:
            nilai = float(s)
        except ValueError:
            print("    Masukkan angka ya, contoh: 2 atau 1e-9")
            continue
        if boleh_negatif and nilai == 0:
            print("    Tidak boleh 0")
            continue
        if not boleh_negatif and nilai <= 0:
            print("    Harus lebih besar dari 0")
            continue
        return nilai


def hitung(ekspresi, data):
    data = dict(data)
    data[eps0] = EPS0
    return float(ekspresi.subs(data))


def judul(teks):
    print("\n" + "=" * 60)
    print(teks)
    print("=" * 60)


def tampil(label, ekspresi):
    print(f"{label} = {sp.simplify(ekspresi)}")


# ======================================================================
# 1. BIDANG
# ======================================================================
def bidang():
    judul("1. BIDANG BERMUATAN")
    print("  a) Bidang tak hingga")
    print("  b) Cakram berjari-jari R (titik di sumbu)")
    pilih = input("  Pilih a/b : ").strip().lower()

    zp, rp = sp.symbols("zp rp", positive=True)

    if pilih == "a":
        E = sigma / (2 * eps0)                       # hukum Gauss
        dV = -sp.integrate(E, (zp, 0, z))            # V(z) - V(0)
        print("\nRumus hasil penurunan:")
        tampil("E        ", E)
        tampil("V(z)-V(0)", dV)
        print("\nMasukkan data:")
        s = baca("sigma, rapat muatan (C/m^2)", True)
        zz = baca("z, jarak dari bidang (m)")
        data = {sigma: s, z: zz}
        print(f"\nE         = {hitung(E, data):.4g} N/C")
        print(f"V(z)-V(0) = {hitung(dV, data):.4g} V")
    else:
        dVr = k * sigma * 2 * sp.pi * rp / sp.sqrt(rp**2 + z**2)
        V = sp.integrate(dVr, (rp, 0, R))
        E = -sp.diff(V, z)
        print("\nRumus hasil penurunan:")
        tampil("V(z)", V)
        tampil("E(z)", E)
        print("\nMasukkan data:")
        s = baca("sigma, rapat muatan (C/m^2)", True)
        RR = baca("R, jari-jari cakram (m)")
        zz = baca("z, jarak di sumbu (m)")
        data = {sigma: s, R: RR, z: zz}
        print(f"\nV(z) = {hitung(V, data):.4g} V")
        print(f"E(z) = {hitung(E, data):.4g} N/C")


# ======================================================================
# 2. TETRAHEDRAL
# ======================================================================
def tetrahedral():
    judul("2. TETRAHEDRAL (4 muatan q di titik sudut)")
    s = a / (2 * sp.sqrt(2))
    titik = [sp.Matrix(v) for v in
             [(s, s, s), (s, -s, -s), (-s, s, -s), (-s, -s, s)]]
    jarak = sp.simplify(titik[0].norm())
    V = sum(k * q / sp.simplify(p.norm()) for p in titik)
    print("\nRumus hasil penurunan:")
    print("Jarak titik sudut ke pusat =", jarak)
    tampil("V pusat", V)
    print("\nMasukkan data:")
    qq = baca("q, muatan tiap titik sudut (C)", True)
    aa = baca("a, panjang rusuk (m)")
    data = {q: qq, a: aa}
    print(f"\nV pusat = {hitung(V, data):.4g} V")


# ======================================================================
# 3. OKTAHEDRAL
# ======================================================================
def oktahedral():
    judul("3. OKTAHEDRAL (6 muatan q di titik sudut)")
    b = a / sp.sqrt(2)
    titik = [sp.Matrix(v) for v in
             [(b, 0, 0), (-b, 0, 0), (0, b, 0), (0, -b, 0), (0, 0, b), (0, 0, -b)]]
    V = sum(k * q / sp.simplify(p.norm()) for p in titik)
    print("\nRumus hasil penurunan:")
    print("Jarak titik sudut ke pusat =", sp.simplify(b))
    tampil("V pusat", V)
    print("\nMasukkan data:")
    qq = baca("q, muatan tiap titik sudut (C)", True)
    aa = baca("a, panjang rusuk (m)")
    data = {q: qq, a: aa}
    print(f"\nV pusat = {hitung(V, data):.4g} V")


# ======================================================================
# 4. BOLA PEJAL
# ======================================================================
def bola():
    judul("4. BOLA PEJAL BERMUATAN HOMOGEN")
    rpp = sp.symbols("rpp", positive=True)
    rho = Q / (sp.Rational(4, 3) * sp.pi * R**3)
    E_luar = k * Q / r**2
    E_dalam = sp.simplify(rho * sp.Rational(4, 3) * sp.pi * r**3
                          / (4 * sp.pi * r**2 * eps0))
    V_luar = -sp.integrate(E_luar.subs(r, rpp), (rpp, sp.oo, r))
    V_dalam = V_luar.subs(r, R) - sp.integrate(E_dalam.subs(r, rpp), (rpp, R, r))
    print("\nRumus hasil penurunan:")
    tampil("E luar  (r>R)", E_luar)
    tampil("E dalam (r<R)", E_dalam)
    tampil("V luar  (r>R)", V_luar)
    tampil("V dalam (r<R)", V_dalam)
    print("\nMasukkan data:")
    QQ = baca("Q, muatan total (C)", True)
    RR = baca("R, jari-jari bola (m)")
    rr = baca("r, jarak titik dari pusat (m)")
    data = {Q: QQ, R: RR, r: rr}
    if rr >= RR:
        print("\nTitik di luar/permukaan bola (r >= R)")
        print(f"V = {hitung(V_luar, data):.4g} V")
        print(f"E = {hitung(E_luar, data):.4g} N/C")
    else:
        print("\nTitik di dalam bola (r < R)")
        print(f"V = {hitung(V_dalam, data):.4g} V")
        print(f"E = {hitung(E_dalam, data):.4g} N/C")


# ======================================================================
# 5. BATANG
# ======================================================================
def batang():
    judul("5. BATANG BERMUATAN")
    print("  a) Titik di perpanjangan batang (jarak d dari ujung)")
    print("  b) Titik di garis bagi tegak lurus (jarak y dari tengah)")
    pilih = input("  Pilih a/b : ").strip().lower()

    xp = sp.symbols("xp", real=True)

    if pilih == "a":
        V = sp.integrate(k * lam / (xp + d), (xp, 0, L))
        print("\nRumus hasil penurunan:")
        print("V = k * lambda * ln((L + d) / d)")
        print("\nMasukkan data:")
        ll = baca("lambda, rapat muatan linear (C/m)", True)
        LL = baca("L, panjang batang (m)")
        dd = baca("d, jarak dari ujung batang (m)")
        data = {lam: ll, L: LL, d: dd}
        print(f"\nV = {hitung(V, data):.4g} V")
    else:
        V = sp.simplify(sp.integrate(k * lam / sp.sqrt(xp**2 + y**2),
                                     (xp, -L / 2, L / 2)))
        print("\nRumus hasil penurunan:")
        tampil("V", V)
        print("\nMasukkan data:")
        ll = baca("lambda, rapat muatan linear (C/m)", True)
        LL = baca("L, panjang batang (m)")
        yy = baca("y, jarak dari tengah batang (m)")
        data = {lam: ll, L: LL, y: yy}
        print(f"\nV = {hitung(V, data):.4g} V")


# ======================================================================
# MENU UTAMA
# ======================================================================
def main():
    menu = {"1": bidang, "2": tetrahedral, "3": oktahedral,
            "4": bola, "5": batang}
    while True:
        judul("PENURUNAN POTENSIAL LISTRIK")
        print("  1. Bidang")
        print("  2. Tetrahedral")
        print("  3. Oktahedral")
        print("  4. Bola pejal")
        print("  5. Batang bermuatan")
        print("  0. Keluar")
        pilih = input("Pilih nomor : ").strip()
        if pilih == "0":
            print("Selesai.")
            break
        if pilih in menu:
            menu[pilih]()
        else:
            print("Pilihan tidak ada, coba lagi.")


if __name__ == "__main__":
    main()