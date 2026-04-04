apel = 12
teman = 4
apel_per_teman = apel / teman
print("Apel per teman:", apel_per_teman)

apel += 8
print("Total apel sekarang:", apel)


tinggi_siti = 160
tinggi_andi = 165

if tinggi_siti > tinggi_andi:
    print("Siti lebih tinggi")
elif tinggi_siti < tinggi_andi:
    print("Andi lebih tinggi")
else:
    print("Tinggi mereka sama")


cuaca_cerah = True
sudah_pr = True

boleh_main = cuaca_cerah and sudah_pr
print("Budi boleh bermain:", boleh_main)


a = 6  
b = 3  

print("AND:", a & b)   
print("OR:", a | b)    
print("XOR:", a ^ b)   


saldo = 50000
saldo += 20000   
saldo -= 30000  

print("Sisa saldo:", saldo)


peserta = ["Andi", "Budi", "Citra", "Dewi"]

print("Apakah Eka terdaftar?", "Eka" in peserta)

kalimat = "Saya suka belajar Python"
print("Apakah 'Python' ada?", "Python" in kalimat)


x = 10
y = 10
print("x is y:", x is y)

list1 = [1, 2, 3]
list2 = [1, 2, 3]
print("list1 is list2:", list1 is list2)


angka = 120
hasil = "Lebih besar dari 100" if angka > 100 else "Tidak lebih besar dari 100"
print(hasil)

nilai = 75
status = "Lulus" if nilai > 70 else "Tidak Lulus"
print(status)