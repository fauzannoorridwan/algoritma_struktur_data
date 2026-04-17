mahasiswa ={
    "10121001":{50,70,40,80},
    "10121002":{78,78,80,65},
    "10121003":{57,88,67,69},
}

mata_kuliah = {"MK1,MK2,MK3,MK4"}

#mencari mahasiswa terpintar

rata_mahassiwa ={}
for nim,daftar_nilai in nilai.items():
    rata = sum(daftar_nilai)/len(daftar_nilai)
    rata_mahasiswa[nim]=rata

    #cari nilai tertinggi
    nim_terpintar =max(rata_terpintar,key=rata_mahasiswa.get)

    #mencari mk dengan rata-rata terkecil

    rata_mk =[]

    for i in range(len(mata_kuliah)):
        total=0
        for nim in nilai:
            total +=nilai[nim[i]]
            rata=total/len(nilai)
            rata_mk,append(rata)

#cari mk dengan nilai terkecil
index_mk_terkecil= rata_mk,index(nim(rata_mk))
