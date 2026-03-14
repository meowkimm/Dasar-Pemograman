tugas = int(input("Masukan nilai tugas : "))
uts = int(input("Masukan nilai uts : "))
uas = int(input("Masukan nilai uas : "))

nilai_akhir = (int(tugas) * 0.3) + (int(uts) * 0.3) + (int(uas) * 0.4)
print("Nilai Akhir", nilai_akhir)

nilai_tugas = 0
nilai_uts = 0
nilai_uas = 0

nilai_tugas = tugas
nilai_uts = uts
nilai_uas = uas

#nilai bonus
if nilai_akhir < 75 and nilai_akhir > 60:
    tugas += 25
    uts += 25
    uas += 25

print("===============================")
print("Nilai setelah bonus")

print("Nilai Tugas : ", nilai_tugas)
print("Nilai uts : ", nilai_uts)
print("Nilai uas : ", nilai_uas)

nilai_akhir = (int(nilai_tugas) * 0.3) + (int(nilai_uts) * 0.4) + (int(nilai_uas) * 0.4)
print("Nilai Akhir", nilai_akhir)

if (int(nilai_akhir) >= 75) and (int(nilai_uas) >= 70):
    print("Lulus Sempurna")
elif nilai_akhir <= 75:
    print("TIdak Lulus")
elif nilai_akhir >= 75:
    print("Lulus")
    
print("===============================")
print("Nilai backup")

nilai_asli = [nilai_tugas],[nilai_uts],[nilai_uas]
nilai_backup = nilai_asli

cek_nilai = nilai_asli
nilai_asli is cek_nilai
nilai_asli is nilai_backup
cek_nilai = nilai_backup == nilai_asli

print("Nilai asli : ", nilai_asli) 
print("Nilai backup : ", nilai_backup) 

if cek_nilai == True:
    print ("Mengacu ke objek yang sama")
else:
    print ("Tidak mengacu pada objek yang sama")

print("===============================")
print("Daftar Keanggotaan")


daftar_murid = ["rizky","fadil","udin"]
print(daftar_murid)
nama = input(str("Masukan nama : "))

if nama in daftar_murid:
    print("Nama ada dalam daftar")
else:
    print("Tidak ada dalam daftar")

print("===============================")
print("Operator bitwise")

angka1 = 10
angka2 = 7
angka3 = 3

print("10 & 7 & 3 = ", angka1 & angka2 & angka3)
print("10 | 7 | 3 = ", angka1 | angka2 | angka3)
print("10 ^ 7 ^ 3 = ", angka1 ^ angka2 ^ angka3)
print("10 << 7 << 3 = ", angka1 << angka2 << angka3)
print("10 >> 7 >> 3 = ", angka1 >> angka2 >> angka3)