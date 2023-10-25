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
print("")
print("")