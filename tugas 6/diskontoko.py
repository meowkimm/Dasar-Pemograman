total = int(input("berapa total belanja kamu : "))

if total >= 500000:
    total *= 0.8
elif total >= 250000:
    total *= 0.9

print("total harga :Rp.", total)