print("-------------- Soal 1 -----------------")
hasil_akhir = [
    {'nama': 'Reza', 'nilai': 70},
    {'nama': 'Ciut', 'nilai': 63},
    {'nama': 'Dian', 'nilai': 80},
    {'nama': 'Badu', 'nilai': 40}
]

for siswa in hasil_akhir:
    if siswa['nilai'] > 65:
        print(siswa['nama'], end="")

print()

print("-------------- Soal 2 -----------------")
list_buah = ["Pepaya", "Mangga", "Pisang", "Durian", "Jambu"]
buah_reverse = []
for buah in reversed(list_buah):
    buah_reverse.append(buah)
print(buah_reverse)

print()

print("-------------- Soal 3 -----------------")
buah_duplikasi = []
for n in list_buah:
    buah_duplikasi.append(n)
    buah_duplikasi.append(n)
print(buah_duplikasi)

print()

print("-------------- Soal 4 -----------------")
nama = "Nurul Fikri"
print(nama.replace("u","").replace("i",""))