
soal1 = "/---------------- Biodata Diri ----------------/"
nama = "Agas Triawan"
nim = "0110223161"
kelas = "TI05"
alamat = "Cimpaeun RT/01 RW/13 No.23 Kelurahan Cimpaeun, Kecamatan Tapos, Kota Depok"
pembatas = "/---------------------------------------------/"

print(soal1)
print("")
print("Nama  :", nama)
print("Nim   :", nim)
print("Kelas :", kelas)
print("Alamat:", alamat)
print("")
print(pembatas)
print("")
print("")


soal2 = "/---------------- Biodata Teman ----------------/"
nama_teman = "Ahmad Hilmi"
nim_teman = "0110223148"
kelas_teman = "TI05"
alamat_teman = "Kampung sugutamu, Depok"

pembatas = "/---------------------------------------------/"

print(soal2)
print("")
print("Nama  :", nama_teman)
print("Nim   :", nim_teman)
print("Kelas :", kelas_teman)
print("Alamat:", alamat_teman)
print("")
print(pembatas)
print("")
print("")


soal3 = "/---------------- Berat Badan Ideal ----------------/"
tinggi_badan = 170  # Tinggi dalam cm
berat_badan = 55  # Berat dalam kg

tinggi_badan_meter = tinggi_badan / 100

# Hitung IMT
berat_badan = berat_badan / (tinggi_badan_meter ** 2)

print(soal3)
print("")
print("Berat Badan anda adalah :", int(berat_badan))
print("Berat Badan Kurang : dibawah 18.5")
print("Berat Badan Ideal : Diatas 18,5 dan Dibawah 22.5")
print("Kelebihan Berat Badan : Diatas 22.5")
print("")
print(pembatas)
print("")
print("")

soal4 = "/---------------- Konversi celcius ke fahreinheit ----------------/"
celcius  = 50  # Tinggi dalam cm
fahrenheit = (celcius * 9/5) + 32

print(soal4)
print("")
print("Jika Celcius =", int(celcius), "Maka Fahrenheit =", int(fahrenheit))
print("")
print(pembatas)
print("")
print("")


soal5 = "/---------------- Luas Keliling Tabung ----------------/"

r = 10
t = 20

# Menghitung luas permukaan tabung
pi = 3.14159  
luas_permukaan = 2 * pi * r * (r + t)

# Menghitung keliling tabung
keliling = 2 * pi * r

print(soal5)
print("Diketahui r = 10 dan t = 20, Maka :")
print("Luas Permukaan Tabung =", int(luas_permukaan))
print("Keliling Tabung =", int(keliling))
print("")
print(pembatas)
print("")
print("")