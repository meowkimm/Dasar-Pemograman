def hitung_total(harga, jumlah):
    return harga * jumlah


def hitung_diskon(total):
    if total >= 100000:
        return total * 0.10
    return 0


def hitung_bayar(total, diskon):
    return total - diskon