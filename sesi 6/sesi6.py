makanan = []

for i in range(10):
    makanan.append(input("masukan nama makanan : "))
    
for item in makanan[::-1]:
    print(item)