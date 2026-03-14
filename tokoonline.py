jmlbarang = int(input("Masukan jumlah barang : "))
harga = int(input("Masukan Harga Barang : "))
status_pelanggan = input(str("Apakah pelanggan member? : "))
kode_diskon = input(str("Masukan kode diskon : "))
total_awal = jmlbarang * harga
total = jmlbarang * harga
print("total belanjaan kamu :",total)

total_diskon = 0

if jmlbarang > 10:
    diskon = 0.05
    jmlbarang
    total_diskon = total_awal * diskon
    print("total diskon :", total_diskon)

total -= total_diskon

print("total harga setelah di kurang diskon :", total)

if total >= 1000000:
    print("pembelian besar")
elif total >= 500000:
    print("pembelian sedang")
elif total < 500000:
    print("pembelian kecil")
    
if (status_pelanggan == "ya") and (total > 500000):
    diskon_tambahan = 0.10
    total_diskon_tambahan = total * diskon_tambahan
    print("total diskon tambahan :",total_diskon_tambahan)
    print("total akhir :",total - total_diskon_tambahan)
    
kode_diskon_valid = ["HEMAT10","PROMO20","SALE30"]

if kode_diskon in kode_diskon_valid:
    print("dapat diskon")


data_pelanggan = [1,2,3,4,5]
data_chace = data_pelanggan

cek_data = data_pelanggan
data_pelanggan is cek_data
data_pelanggan is data_chace
cek_data = data_chace == data_pelanggan


print("data pelanggan :",data_pelanggan)
print("data chace :",data_chace)

if cek_data == True:
    print ("keduanya merupakan objek yang sama")
else:
    print("keduanya tidak sama")

kode_masuk = 12
kode_izin = 10

print("12 & 10 =",kode_masuk & kode_izin)
print("12 | 10=",kode_masuk | kode_izin)
print("12 ^ 10 =",kode_masuk ^ kode_izin)
print("12 << 10=",kode_masuk << kode_izin)
print("12 >> 10 =",kode_masuk >> kode_izin)