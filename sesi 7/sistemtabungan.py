total = 0
hari = 0

target = int(input("Masukan Target Tabungan : Rp."))

while total < target:
    hari += 1
    print("Hari ke - ", hari)
    
    nabung = int(input("Masukan jumlah tabungan : "))
    total += nabung
    
    print("Total Tabungan Sementara : Rp.", total)
    
    if total < target:
        sisa = target - total
        print("Sisa yang harus dikumpulkan : Rp.", sisa)
    else:
        print("Target tabungan sudah tercapai")

print("Total hari yang diperlukan : ", hari)
    