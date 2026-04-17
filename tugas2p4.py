x = int(input("Masukkan jumlah hari proyek: "))
tahun = x // 365
sisa = x % 365
bulan = sisa // 30
hari = sisa % 30
print(f"Proyek dikerjakan selama ({tahun} tahun, {bulan} bulan, {hari} hari)")
