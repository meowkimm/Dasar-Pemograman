namaBuah = ["Apel", "Jeruk", "Pisang", "Mangga"]
stok = [30, 30, 30, 30]

# Tampilkan stok awal
total = 0
for i in range(4): 
    if stok[i] < 5:
        print(namaBuah[i] + ":", stok[i], "- Stok rendah!")
    else:
        print(namaBuah[i] + ":", stok[i])
    total += stok[i]

print("Total stok awal:", total)

# Update stok
while True:
    pilih = int(input("Pilih buah (0-3) atau -1 untuk selesai: "))
    
    if pilih == -1:
        break
    
    tambah = int(input("Tambah berapa? "))
    stok[pilih] += tambah
    
# Hitung total akhir dan stok rendah
total = 0
rendah = 0

for i in range(4):
    total += stok[i]
    if stok[i] < 5:
        rendah += 1
        
print("\nStok")
for i in range(4):
    print(namaBuah[i], ":", stok[i])
    
print("Total akhir:", total)
print("Jumlah buah stok rendah:", rendah)

print("Stok Rendah : ")
for i in range(4):
    if stok[i] < 5:
        print(namaBuah[i])