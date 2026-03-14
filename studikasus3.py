name = "Muhammad Rizky Adianto"
age = 20
address = "Kp. Cimelati"
province = "Jawa Barat"
scorepython = 95

print("Nama : ", name, type(name))
print("Umur : ", age, type(age))
print("Alamat : ", address, type(address))
print("Provinsi : ", province, type(province))
print("Scorepython : ", scorepython, type(scorepython))

print("====================================================")

#konversi
a = 14
b = "25"
c = 3.3
d = True

#int ke str, float, bool
print(str(a), type(str(a)))
print(float(a), type(float(a)))
print(bool(a), type(bool(a)))

print("====================================================")

#str ke int, float, bool
print(int(b), type(int(b)))
print(float(b), type(float(b)))
print(bool(b), type(bool(b)))

print("====================================================")

#float ke int, str, bool
print(int(c), type(int(c)))
print(str(c), type(str(c)))
print(bool(c), type(bool(c)))

print("====================================================")

#bool ke int, str, float
print(int(d), type(int(d)))
print(str(d), type(str(d)))
print(float(d), type(float(d)))

print("====================================================")
#tipe data desimal, oktal, hexadesimal, biner

angka_desimal = 22
angka_oktal = 0o26
angka_hexadesimal = 0x16
angka_biner = 0b10110

print("Desimal : ", angka_desimal)
print("Oktal : ", angka_oktal)
print("Hexadesimal : ", angka_hexadesimal)
print("Biner : ", angka_biner)

print("====================================================")
#list, tuple, dictionary, list of dictionary

#list
nama = ["rizky", "udin", "fadil"]
print(nama)
print("====================================================")

#tuple
nasi_goreng = ("Nasi", "Kecap", "Telur", "Garem")
print(nasi_goreng)
print("====================================================")

#dictionary
mahasiswa = {
    "Nama": "Muhammad Rizky",
    "Umur": 20,
    "Prodi": "Teknik Informatika"
}

print(mahasiswa)
print("====================================================")

#list of dictionary
kelas = [
    {"Nama": "Warda Amalia", "Umur": 18, "Prodi": "Teknik Informatika"},
    {"Nama": "Fadhil Saputra", "Umur": 19, "Prodi": "Teknik Informatika"},
    {"Nama": "Rafly Awaludin", "Umur": 18, "Prodi": "Teknik Informatika"}
]

print(kelas)