print("Selamat datang!")

print("---Menu---")
print("1. Daftar Kontak")
print("2. Tambah Kontak")
print("3. Keluar")


kontak_dict = {
    "nama" : "grace",
    "nomor" : 6289602596004
}

kontak_list = []


while True :
    pilih = int(input("Pilih menu: "))

    if pilih == 1 :
        for i in kontak_dict : 
            print("Nama: ",kontak_dict["nama"])
            print("Nomor Telepon :" ,kontak_dict["nomor"])
        for i in kontak_list:
            print("Nama: ",kontak_list["nama"])
            print("Nomor Telepon: ",kontak_list["nomor"])

    elif pilih == 2 :
        for i in range(1) :
            nama = input("Nama: ")
            nomor = input("No Telepon: ")
            data = {
                "nama" : nama,
                "nomor" : nomor,
            }
            kontak_list.append(data)
            print("Kontak berhasil ditambahkan")

    elif pilih == 3 :
        print("Program selesai, sampai jumpa!")
        break

    else :
        print("Menu tidak tersedia")




