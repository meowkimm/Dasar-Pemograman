# function untuk membalik setiap kata dalam kalimat tanpa mengubah urutan kata dalam kalimat
def reverse_per_kata(kalimat):
    # memisahkan kalimat menjadi beberapa kata
    kata_kata = kalimat.split()

    # list untuk menyimpan kata yang sudah dibalik
    hasil = []

    # membalik setiap kata satu per satu
    for kata in kata_kata:
        hasil.append(kata[::-1])

    # menggabungkan kembali kata kata menjadi satu kalimat
    return " ".join(hasil)


# function untuk mengurutkan kata berdasarkan indeks yang diberikan angka pada list urutan dimulai dari 1, sehingga dikurangi 1 saat mengakses list
def urutkan_kalimat(kalimat, urutan):
    # memisahkan kalimat menjadi beberapa kata
    kata_kata = kalimat.split()

    # list untuk menyimpan kata sesuai urutan baru
    hasil = []

    # mengambil kata berdasarkan indeks pada list urutan
    for indeks in urutan:
        hasil.append(kata_kata[indeks - 1])

    # menggabungkan kembali kata kata menjadi satu kalimat
    return " ".join(hasil)


# Function untuk mengganti huruf vokal dengan simbol tertentu 
# Opsi 1 mengganti vokal kecil, sedangkan opsi 2 mengganti vokal kapital
def ganti_vokal(kalimat, opsi):
    
    # menentukan huruf vokal dan simbol penggantinya
    vokal_kecil = "aiueo"
    vokal_besar = "AIUEO"
    simbol = ["4", "1", "|_|", "3", "0"]

    # variabel untuk menyimpan hasil akhir
    hasil = ""

    # memeriksa setiap karakter dalam kalimat
    for karakter in kalimat:
        if opsi == 1 and karakter in vokal_kecil:
            indeks = vokal_kecil.index(karakter)
            hasil += simbol[indeks]

        elif opsi == 2 and karakter in vokal_besar:
            indeks = vokal_besar.index(karakter)
            hasil += simbol[indeks]

        else:
            # Karakter yang tidak perlu diganti tetap ditambahkan
            hasil += karakter

    return hasil


# Uji coba function reverse_per_kata()
print(reverse_per_kata("AKU CINTA KAMU"))

# Uji coba function urutkan_kalimat()
print(urutkan_kalimat("HARI INI SEDANG BELAJAR PYTHON", [5, 1, 4, 3, 2]))

# Uji coba function ganti_vokal() dengan opsi 1
print(ganti_vokal("Aku Cinta Kamu", 1))

# Uji coba function ganti_vokal() dengan opsi 2
print(ganti_vokal("Aku Cinta Kamu", 2))