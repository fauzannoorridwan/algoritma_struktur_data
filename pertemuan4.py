namakaryawan = str(input("Masukkan nama karyawan: "))
gajipokok = float(input("Masukkan gaji pokok: "))

persentunjangan = 0.2
persenpajak = 0.15

tunjangan =(persentunjangan)*(gajipokok)
pajak = (persenpajak)*(gajipokok + tunjangan)
gajibersih = gajipokok + tunjangan - pajak
print("Nama Karyawan:", namakaryawan)
print("Gaji bersih:", gajibersih) 