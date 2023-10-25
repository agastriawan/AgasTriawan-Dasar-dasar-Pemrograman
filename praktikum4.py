soal1 = "/---------------- Soal 1 || Berat Badan Ideal ----------------/"
print(soal1)
tinggi_badan = float(input("Masukan Tinggi Badan (dalam cm): "))  
berat_badan = float(input("Masukan Berat Badan (dalam kg): "))  

tinggi_badan_meter = tinggi_badan / 100

# Hitung IMT
berat_badan = berat_badan / (tinggi_badan_meter ** 2)
    
if berat_badan < 18.5:
    print(soal1)
    print("Berat Badan Anda Adalah:", int(berat_badan), "|| Berat Badan Anda Kurang : Dibawah 18.5")
elif 18.5 <= berat_badan < 22.5:
    print(soal1)
    print("Berat Badan Anda Adalah:", int(berat_badan), "|| Berat Badan Ideal : Diatas 18.5 dan Dibawah 22.5")
else:
    print(soal1)
    print("Berat Badan Anda Adalah:", int(berat_badan), "|| Kelebihan Berat Badan : Diatas 22.5")


soal2 = "/---------------- Soal 2 || Bilangan Positif & Negatif ----------------/"

print(soal2)
bilangan = float(input("Masukan Bilangan: "))

if bilangan != int(bilangan):
    print("Bilangan anda bukan bilangan bulat, masukan kembali bilangan anda")
    bilangan = float(input("Masukan Bilangan: "))

if bilangan < 0:
    print(soal2)
    print("Bilangan Anda Adalah:", int(bilangan), "|| Bilangan Anda adalah Negatif")
elif bilangan > 0:
    print(soal2)
    print("Bilangan Anda Adalah:", int(bilangan), "|| Bilangan Anda adalah Positif")
else:
    print(soal2)
    print("Bilangan Anda Adalah:", int(bilangan), "|| Bilangan Anda adalah Nol")


soal3 = "/---------------- Soal 3 || Batu Gunting Kertas ----------------/"

print(soal3)
jenis_suit_1 = input("Jenis Suit Orang Pertama (Batu, Gunting, atau Kertas): ")
jenis_suit_2 = input("Jenis Suit Orang Kedua (Batu, Gunting, atau Kertas): ")

if jenis_suit_1 == jenis_suit_2:
    print(soal3)
    print("Hasilnya adalah Seri. Kedua pemain memilih", jenis_suit_1)
elif jenis_suit_1 == "Batu" and jenis_suit_2 == "Gunting" or jenis_suit_1 == "Gunting" and jenis_suit_2 == "Kertas" or jenis_suit_1 == "Kertas" and jenis_suit_2 == "Batu":
    print(soal3)
    print("Pemenangnya adalah Orang Pertama dengan pilihan", jenis_suit_1)
else:
    print(soal3)
    print("Pemenangnya adalah Orang Kedua dengan pilihan", jenis_suit_2)

