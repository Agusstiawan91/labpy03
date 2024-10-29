def cari_bilangan_terbesar():
    bilangan_terbesar = None

    while True:
        angka = int(input("Masukkan bilangan: "))
        
        if angka == 0:
            break
        
        if bilangan_terbesar is None or angka > bilangan_terbesar:
            bilangan_terbesar = angka

    if bilangan_terbesar is not None:
        print("Bilangan terbesar adalah:", bilangan_terbesar)
    else:
        print("Tidak ada angka yang dimasukkan.")

cari_bilangan_terbesar()
