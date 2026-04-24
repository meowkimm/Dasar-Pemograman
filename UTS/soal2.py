namaKandang = str(input("Nama Kandang : "))
jumlahAyam = int(input("Jumlah ayam : "))
jumlahTelur = int(input("Jumlah Telur yang dihasilkan : "))

hari = 0
total_harian = 0

while hari <= 7:
    hari += 1
    jumlahTelur = int(input(f"Jumlah Telur yang dihasilkan pada hari ke {hari}  : "))
    total_harian += jumlahTelur
    print(f"Total Harian pada hari ke {hari} : ",total_harian)
    
        
        
    if hari == 7:
        total = total_harian

        rata = total / jumlahAyam
        
        print("Rata-Rata Telur",rata)
        print("\nTotal Produksi selama 7 hari : ", total)

        if rata >= 0.8:
            print("Produktif Tinggi")
        elif rata == 0.5 and rata == 0.79:
            print("Produktif Sedang")
        elif rata == 0:
            print("Produktif Rendah")
        break
        
        
    
        

    