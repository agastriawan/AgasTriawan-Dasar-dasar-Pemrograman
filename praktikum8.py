# def hello():
#     print("Hello 1")
#     print("Hello 2")

# def panggil():
#     hello()
#     print("Saya Kelas TI 05")
    
# def say(nama, prodi):
#     print("Hello nama saya", nama)
#     print("Prodi saya adalah", prodi)
    
# def tambah(a, b):
#     jumlah = a + b
#     print(jumlah)
    
# def luas_persegi(sisi):
#     return sisi*sisi

# def pangkat(a, b):
#     return a ** b
    

# print("Pangkat",pangkat(2,3))
# print("Luas Persegi Adalah ", luas_persegi(3))

# TUGAS PRAKTIKUM

soal1 = "/---------------- Soal 1 ----------------/"
print(soal1)
def data_diri(nama, alamat, gender, umur, hoby):
    print("Nama :", nama)
    print("Alamat :", alamat)
    print("Gender :", gender)
    print("Umur :", umur)
    print("Hoby :", hoby)

data_diri("Agas Triawan", "Tapos, Depok", "Laki-Laki", 17, "Mendengarkan Musik")

print("\n")
soal2 = "/---------------- Soal 2 ----------------/"
print(soal2)

def mencari_nilai(nilai):
    if nilai < 60:
        print("Nilai Anda Adalah:", int(nilai), "|| Nilai Anda Gagal")
    elif 61 <= nilai <= 70:
        print("Nilai Anda Adalah:", int(nilai), "|| Nilai Anda Baik")
    elif 71 <= nilai <= 80:
        print("Nilai Anda Adalah:", int(nilai), "|| Nilai Anda Sangat Baik")
    elif 81 <= nilai <= 100:
        print("Nilai Anda Adalah:", int(nilai), "|| Nilai Anda Istimewa")
    else:
        print("Input tidak valid. Masukkan nilai antara 0 dan 100.")


nilaisiswa = float(input("Masukkan Nilai Anda: "))
mencari_nilai(nilaisiswa)


print("\n")
soal3 = "/---------------- Soal 3 ----------------/"
print(soal3)
def mencari_ganjil(angka):
    number = 1
    while number <= angka:
        print(number, end=', ')
        number += 2

nilaiganjil = float(input("Masukkan Angka: "))
mencari_ganjil(nilaiganjil)




