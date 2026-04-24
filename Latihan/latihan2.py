barang = [
    ("Indomie Goreng", 3500), ("Indomie Rebus", 4000), ("Air Mineral", 1500)
]

pelanggan = 0

print("Nama Barang : ")
for i in range (8):
    print(i+1, "." ,barang[i], "-", harga[i])

jumlah = int(input("Masukan Jumlah barang yang kamu beli : "))
keranjang = []

for barang in range (jumlah):
    pilih = int(input("Pilih Barang : "))
    
for i in range (jumlah):