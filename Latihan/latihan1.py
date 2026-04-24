nilai_akhir = 0
percobaan = 0

while nilai_akhir < 85:
    percobaan += 1
    print("Percobaan ke - ", percobaan)
    
    uts = float(input("Masukan nilai UTS : "))
    uas = float(input("Masukan nilai UAS : "))
    project = float(input("Masukan nilai Project : "))
    
    nilai_akhir = ((uts * 0.3) + (uas * 0.4) + (project * 0.3))
    
    print("Nilai Akhirnya : ", round(nilai_akhir, 2))
    
    if nilai_akhir < 85:
        print("Belum lulus")
    else:
        print("Selamat Anda Lulus")
        
print("Mahasiswa lulus pada percobaan ke ", percobaan)