jarak = int(input("masukan jarak : "))

if jarak <= 5:
    tarif = 5000
elif jarak < 10:
    tarif = 4000
else:
    tarif = 3000

total = tarif * jarak
print("total tarif :Rp.", total)