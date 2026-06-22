import matplotlib.pyplot as plt

nama_file = "penjualan_fore.txt"


def tambah_data():
    try:
        menu = input("Masukkan nama menu kopi: ")
        jumlah = int(input("Masukkan jumlah penjualan: "))

        with open(nama_file, "a") as file:
            file.write(f"{menu},{jumlah}\n")

        print("Data berhasil disimpan!")

    except ValueError:
        print("Jumlah penjualan harus berupa angka!")


def tampilkan_data():
    try:
        with open(nama_file, "r") as file:
            data = file.readlines()

        if not data:
            print("Data masih kosong.")
            return 

        print("\nData Penjualan Fore Coffee:")
        for baris in data:
            menu, jumlah = baris.strip().split(",")
            print(f"Menu: {menu}, Jumlah Terjual: {jumlah}")

    except FileNotFoundError:
        print("File belum tersedia. Silakan tambah data terlebih dahulu.")


def tampilkan_grafik():
    try:
        menu_list = []
        jumlah_list = []

        with open(nama_file, "r") as file:
            data = file.readlines()

        if not data:
            print("Data masih kosong, grafik tidak dapat ditampilkan.")
            return

        for baris in data:
            menu, jumlah = baris.strip().split(",")
            menu_list.append(menu)
            jumlah_list.append(int(jumlah))

        plt.bar(menu_list, jumlah_list)
        plt.title("Grafik Penjualan Fore Coffee")
        plt.xlabel("Menu Kopi")
        plt.ylabel("Jumlah Terjual")
        plt.show()

    except FileNotFoundError:
        print("File belum tersedia. Silakan tambah data terlebih dahulu.")
    except ValueError:
        print("Data di dalam file tidak valid.")


def menu_utama():
    while True:
        print("\n=== Program Penjualan Fore Coffee ===")
        print("1. Tambah Data Penjualan")
        print("2. Tampilkan Data Penjualan")
        print("3. Tampilkan Grafik Penjualan")
        print("4. Keluar")

        pilihan = input("Pilih menu: ")

        if pilihan == "1":
            tambah_data()
        elif pilihan == "2":
            tampilkan_data()
        elif pilihan == "3":
            tampilkan_grafik()
        elif pilihan == "4":
            print("Program selesai. Terima kasih!")
            break
        else:
            print("Pilihan tidak tersedia!")


menu_utama()