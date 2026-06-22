from makanan import Makanan
from hitung import hitung_total, hitung_diskon, hitung_bayar

menu = {
    1: ("Nasi Goreng", 15000),
    2: ("Ayam Geprek", 20000),
    3: ("Mie Ayam", 12000),
    4: ("Bakso", 18000)
}

print("SISTEM PEMESANAN MAKANAN")

nama = input("Masukkan nama pelanggan: ")

print("\nDaftar Menu:")
for kode, data in menu.items():
    print(f"{kode}. {data[0]} - Rp {data[1]}")

pilihan = int(input("\nPilih menu 1/2/3/4: "))
jumlah = int(input("Masukkan jumlah pesanan: "))

nama_makanan = menu[pilihan][0]
harga = menu[pilihan][1]

pesanan = Makanan(nama, nama_makanan, harga, jumlah)

total_awal = hitung_total(pesanan.harga, pesanan.jumlah)
diskon = hitung_diskon(total_awal)
total_bayar = hitung_bayar(total_awal, diskon)

print("DETAIL PESANAN MAKANAN")
print("Nama Pelanggan :", pesanan.nama_pelanggan)
print("Nama Makanan   :", pesanan.nama_makanan)
print("Harga Makanan  : Rp", pesanan.harga)
print("Jumlah Pesanan :", pesanan.jumlah)
print("Total Awal     : Rp", total_awal)
print("Diskon         : Rp", diskon)
print("Total Bayar    : Rp", total_bayar)