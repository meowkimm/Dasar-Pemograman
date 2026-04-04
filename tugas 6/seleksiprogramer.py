coding = int(input("nilai coding : "))
interview = input("nilai interview : ")

if (coding >= 60 and interview == "A") or (coding > 80 and interview == "B"):
    print("lolos")
else:
    print("gagal")