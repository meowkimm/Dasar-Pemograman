usia = int(input("masukan usia anda : "))

if usia <= 12:
    harga = 10000 * 0.5
elif usia >= 60:
    harga = 20000 * 0.7
elif usia <= 17:
    harga = 25000
else:
    harga = 30000

print("total harga :Rp.", harga)