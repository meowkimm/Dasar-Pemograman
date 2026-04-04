nilai_rapor = int(input("masukan nilai rapor : "))
penghasilan = int(input("masukan penghasilan : "))

if nilai_rapor >= 90 and penghasilan < 5000000:
    print("mendapat beasiswa penuh")
elif nilai_rapor >= 85 and penghasilan < 8000000:
    print("mendapat beasiswa 50%")
else:
    print("tidak mendapat beasiswa")