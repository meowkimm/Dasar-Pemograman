nama = input("Masukkan nama : ")
umur = input("Masukkan umur : ")
alamat = input("Masukkan alamat : ")
universitas = input("Masukkan universitas : ")

print("\n=== Biodata ===")
print("Nama : {}".format(nama))
print("Umur : {}".format(umur))
print("Alamat : {}".format(alamat))
print("Universitas : {}".format(universitas))

kalimat = "UNIVERSITAS NUSA PUTRA SUKABUMI"

if universitas.upper() == kalimat:
    kata = kalimat.split()

    # a. putra nusa
    print("a.", "{} {}".format(kata[2].lower(), kata[1].lower()))

    # b. NIVERSITAS NSA PTRA SKABMI
    print("b.", "{}".format(kalimat.replace("U", "")))

    # c. SUKABUMI PUTRA NUSA UNIVERSITAS
    print("c.", "{} {} {} {}".format(kata[3], kata[2], kata[1], kata[0]))

    # d. UNPS
    print("d.", "{}".format("".join([k[0] for k in kata])))

    # e. TAS SAPU BUMI
    print("e.", "{} {} {}".format(kalimat[8:11], kalimat[14:16] + kalimat[17:19], kalimat[-4:]))

else:
    print("Universitas tidak sesuai")