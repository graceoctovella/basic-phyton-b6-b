teori = float(input("masukkan nilai ujian teori : "))
praktek = float(input("masukkan nilai ujian praktek : "))

if teori >= 70 and praktek >= 70:
    print("Selamat, Anda lulus! ")
elif teori >= 70 and praktek < 70:
    print("Anda harus mengulang ujian praktek. ")
elif teori < 70 and praktek >= 70:
    print("Anda harus mengulang ujian teori. ")
else:
    print("Anda harus mengulang ujian teori dan praktek. ")