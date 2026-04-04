jenis = input("masukan jenis kendaraan : ")
lama = int(input("berapa lama parkir : "))

if jenis == "motor":
    total = lama * 2000
elif jenis == "mobil":
    total = lama * 5000

print("total biaya parkir :Rp.", total)