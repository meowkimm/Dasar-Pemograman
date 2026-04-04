kategori = input("masukan kategori film : ")
umur = int(input("masukan umur : "))

if kategori == "semua umur":
    print("boleh ditonton siapa saja")
elif kategori == "remaja" and umur >= 13:
    print("boleh ditonton 13+")
elif kategori == "dewasa" and umur >= 18:
    print("boleh ditonton 18+")
else:
    print("tidak boleh nonton")