while True:    
    totalBelanja = int(input("Masukan Total Belanjaan = Rp."))
    totalUang = int(input("Masukan Uang Belanja = Rp."))

    if totalBelanja < totalUang:
        uangKembali = totalUang - totalBelanja
        print(f"total kembalian = {uangKembali}")

        rupiah = [500, 1000, 2000, 5000, 10000, 20000, 50000, 100000]

        for nominal in sorted(rupiah, reverse=True):
            
            if uangKembali >= nominal != 500:
                jumlah = uangKembali // nominal
                print(f"{jumlah} lembar Rp. {nominal} ")

            if nominal == 500:
                print(f"{jumlah} koin Rp. {nominal} ")
            uangKembali %= nominal
                
    else:
        print("tidak ada kembalian!")

    ulangi = input("ulangi proses? y/n = ")
    if ulangi.lower() != "y":
        break


