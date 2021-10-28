saldo_umum=0
saldo_tabungan=0

menu = None
while True:
    print("====== Aplikasi Pencatatan Uang Digital ======")
    print("[1] Informasi Saldo")
    print("[2] Tambah Saldo")
    print("[3] Ambil Saldo")
    print("[0] Keluar")
    print("=============================================")

    menu =int (input(' Pilih menu: '))
    print() 
    if menu == 1:
        print(f"Saldo Umum Anda Saat Ini Adalah: Rp.{saldo_umum},-")
        print(f"Saldo Tabungan Anda Saat Ini Adalah: Rp.{saldo_tabungan},-")
        print()
        print()
    elif menu == 2:
        print("[1] Umum")
        print("[2] Tabungan")
        print("=============================================")
        saldo_tabungan=0
        saldo_umum=0
        menu2=int(input("Pilih Penyimpanan: "))
        if menu2== 1:
            setor = int(input("Nominal Uang Yang Akan Ditambahkan: "))
            saldo_umum=saldo_umum+setor
            print()
            print(f"Penambahan Saldo Anda Sebesar Rp. {setor},- berhasil!")
            print(f"Saldo Umum Anda Saat Ini Adalah: Rp. {saldo_umum},-")
            print(f"Saldo Tabungan Anda Saat Ini Adalah: Rp. {saldo_tabungan},-")
            print("=============================================")
            print()
            print()
        elif menu2==2:
            setor2 = int(input("Nominal Uang Yang Akan Ditambahkan: "))
            saldo_tabungan=saldo_tabungan+setor
            print()
            print(f"Penambahan Saldo Anda Sebesar Rp. {setor2},- berhasil!")
            print(f"Saldo Umum Anda Saat Ini Adalah: Rp. {saldo_umum},-")
            print(f"Saldo Tabungan Anda Saat Ini Adalah: Rp. {saldo_tabungan},-")
            print("=============================================")
            print()
            print()
    elif menu == 3:
        print("[1] Umum")
        print("[2] Tabungan")
        print("=============================================")
        menu3=input("Pilih Penyimpanan: ")
        if menu3 == '1':
            if saldo_umum < 50.000:
                print("Maaf Saldo anda tidak mencukupi")
                print("Silahkan isi saldo terlebih dahulu")
            else:
                print("Jumlah Nominal Penarikan Sebesar 50000, 100000, 250000, 500000, 1000000")
                tunai = int(input("Nominal Uang Yang Akan Diambil: "))
                if (tunai == 50000) or (tunai==100000) or (tunai==250000) or (tunai==500000) or (tunai==10000000):
                    saldo_umum=saldo_umum-tunai
                    print()
                    print(f"Penambahan Saldo Anda Sebesar Rp. {tunai},- berhasil!")
                    print(f"Saldo Umum Anda Saat Ini Adalah: Rp. {saldo_umum},-")
                    print(f"Saldo Tabungan Anda Saat Ini Adalah: Rp. {saldo_tabungan},-")
                    print("=============================================")
        elif menu3 == '2':
            if saldo_tabungan < 50.000:
                print("Maaf Saldo anda tidak mencukupi")
                print("Silahkan isi saldo terlebih dahulu")
            else:
                print("Jumlah Nominal Penarikan Sebesar 50000, 100000, 250000, 500000, 1000000")
                tunai = int(input("Nominal Uang Yang Akan Diambil: "))
                if (tunai == 50000) or (tunai==100000) or (tunai==250000) or (tunai==500000) or (tunai==10000000):
                    saldo_tabungan=saldo_tabungan-tunai
                    print()
                    print(f"Penambahan Saldo Anda Sebesar Rp. {tunai},- berhasil!")
                    print(f"Saldo Umum Anda Saat Ini Adalah: Rp. {saldo_umum},-")
                    print(f"Saldo Tabungan Anda Saat Ini Adalah: Rp. {saldo_tabungan},-")
                    print("=============================================")
                    print()
                    print()

    elif menu== 0:
        print("Terimakasih telah Menggunakan Layanan Kami")
        print()