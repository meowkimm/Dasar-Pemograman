nomor = int(input("Masukkan nomor punggung: "))

if nomor % 2 == 0:
    posisi = "Target Attacker"
    if 50 <= nomor <= 100:
        posisi = "Captain Team"
else:
    posisi = "Defender"
    if nomor > 90:
        posisi = "Playmaker"
    if nomor % 3 == 0 and nomor % 5 == 0:
        posisi = "Keeper"

print("Posisi:", posisi)