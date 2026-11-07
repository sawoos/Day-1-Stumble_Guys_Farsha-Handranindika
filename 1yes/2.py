score = float(input("Masukkan NILAI LO: "))

if score < 0 or score > 100:
    print("erorrr")
elif score >= 85:
    print("A")
elif score >= 75:
    print("B")
elif score >= 65:
    print("C")
elif score >= 50:
    print("D")
else:
    print("E")


total = float(input("Masukkan total belanja: "))
status = input("Apakah member? (y/n): ").strip().lower()
member = status == 'y'

if member:
    if total >= 1000000:
        rate = 0.20
    elif total >= 500000:
        rate = 0.15
    else:
        rate = 0.10
else:
    if total >= 1000000:
        rate = 0.10
    elif total >= 500000:
        rate = 0.05
    else:
        rate = 0.00

diskon = total * rate
total_bayar = total - diskon

print(f"Rate Diskon: {rate * 100}%")
print(f"Diskon: Rp {diskon:,.2f}")
print(f"Total Bayar: Rp {total_bayar:,.2f}")