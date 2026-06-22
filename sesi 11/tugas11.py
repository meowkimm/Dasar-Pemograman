nama_cafe = "cafe sejahtera"; #varibel global

#fungsi sederhana
def cafe():
    print("selamat datang di cafe :", nama_cafe)
    print("cafe dengan sejuta rasa")

cafe()

#fungsi dengan parameter
print("===========================")
def pesanan(nama_pelanggan, minuman):
    print(f"Pelanggan {nama_pelanggan} Memesan Minuman {minuman}")

pesanan("Rizky","Kopi Susu")
pesanan("Mpud","Kopi Liong")
pesanan("Bejo","Butterscotch")
pesanan("Hari","Citrus")

#parameter opsional
print("===========================")
def layanan(layanan="ambil sendiri"):
    print(f"layanan : {layanan}")

#default    
layanan()
#diisi
layanan("Take Away")

#parameter tidak berurutan
print("===========================")
pesanan(
    minuman = "Kopi Susu", nama_pelanggan = "Rizky"
)

#fungsi dengan parameter wajib & return
print("===========================")
def pembayaran(harga, jumlah):
    total = harga * jumlah #variabel lokal
    pajak = total * 0.11
    return total, pajak

total_bayar, pajak = pembayaran(25000, 2) 

print("Total Bayar senilai", total_bayar)
print("Pajaknya :", pajak)

