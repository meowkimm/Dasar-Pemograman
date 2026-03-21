# 1. Operator Aritmatika
apel = 12
teman = 4
apel_per_teman = apel / teman
print("Apel per teman:", apel_per_teman)

apel += 8
print("Total apel sekarang:", apel)


# 2. Operator Perbandingan
tinggi_siti = 160
tinggi_andi = 165

if tinggi_siti > tinggi_andi:
    print("Siti lebih tinggi")
elif tinggi_siti < tinggi_andi:
    print("Andi lebih tinggi")
else:
    print("Tinggi mereka sama")


# 3. Operator Logika
cuaca_cerah = True
sudah_pr = True

boleh_main = cuaca_cerah and sudah_pr
print("Budi boleh bermain:", boleh_main)


# 4. Operator Bitwise
a = 6  
b = 3  

print("AND:", a & b)   
print("OR:", a | b)    
print("XOR:", a ^ b)   


# 5. Operator Penugasan
saldo = 50000
saldo += 20000   
saldo -= 30000  

print("Sisa saldo:", saldo)


# 6. Operator Keanggotaan
peserta = ["Andi", "Budi", "Citra", "Dewi"]

print("Apakah Eka terdaftar?", "Eka" in peserta)

kalimat = "Saya suka belajar Python"
print("Apakah 'Python' ada?", "Python" in kalimat)


# 7. Operator Identitas
x = 10
y = 10
print("x is y:", x is y)

list1 = [1, 2, 3]
list2 = [1, 2, 3]
print("list1 is list2:", list1 is list2)


# 8. Operator Ternary
angka = 120
hasil = "Lebih besar dari 100" if angka > 100 else "Tidak lebih besar dari 100"
print(hasil)

nilai = 75
status = "Lulus" if nilai > 70 else "Tidak Lulus"
print(status)