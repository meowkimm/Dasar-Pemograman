usia = int(input("masukan usia : "))

if usia <= 12 :
    print("anak-anak")
elif usia <= 17:
    print("remaja")
elif usia <= 59:
    print("dewasa")
elif usia >= 60:
    print("lansia")
else:
    print("masukan angka")