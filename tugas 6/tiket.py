total_semua = 0

# LOKET 1
print("LOKET 1")
usia_1 = int(input("masukan usia anda : "))
if usia_1 <=12 :
    jmlh = int(input("jumlah orang : "))
    total = jmlh * 10000
elif usia_1 <=17 :
    jmlh = int(input("jumlah orang : "))
    total = jmlh * 15000
elif usia_1 <= 59:
    jmlh = int(input("jumlah orang : "))
    total = jmlh * 25000
else:
    total = 0
print("total harga :Rp.", total)
total_semua += total

# LOKET 2
print("LOKET 2")
usia_2 = int(input("masukan usia anda : "))
if usia_2 <=12 :
    jmlh = int(input("jumlah orang : "))
    total = jmlh * 10000
elif usia_2 <=17 :
    jmlh = int(input("jumlah orang : "))
    total = jmlh * 15000
elif usia_2 <= 59:
    jmlh = int(input("jumlah orang : "))
    total = jmlh * 25000
else:
    total = 0
print("total harga :Rp.", total)
total_semua += total

# LOKET 3
print("LOKET 3")
usia_3 = int(input("masukan usia anda : "))
if usia_3 <=12 :
    jmlh = int(input("jumlah orang : "))
    total = jmlh * 10000
elif usia_3 <=17 :
    jmlh = int(input("jumlah orang : "))
    total = jmlh * 15000
elif usia_3 <= 59:
    jmlh = int(input("jumlah orang : "))
    total = jmlh * 25000
else:
    total = 0
print("total harga :Rp.", total)
total_semua += total

print("total pembayaran :Rp.", total_semua)