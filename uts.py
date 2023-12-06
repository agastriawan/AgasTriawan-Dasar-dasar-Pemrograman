
# # Contoh Variable Benar 
# nama = "Agas Triawan"
# umur = 17
# tinggi_badan = 172



# # Contoh Variable Salah

# @#%variabel = 10 # Salah (menggunakan karakter khusus)
# 2_variabel = "contoh" # Salah (dimulai dengan angka)
# nama depan = "Alice" # Salah (menggunakan spasi)

# # Salah (tipe data tidak konsisten)
# angka = 5
# angka = "lima"

# Input panjang diagonal 1 dan diagonal 2 dari layang-layang
# diagonal1 = float(input("Masukkan panjang diagonal 1: "))
# diagonal2 = float(input("Masukkan panjang diagonal 2: "))

# sisi = ((diagonal1/2)**2 + (diagonal2/2)**2)**0.5

# luas_layang_layang = 0.5 * diagonal1 * diagonal2
# keliling_layang_layang = 2 * sisi

# # Tampilkan hasil
# print(f"Luas layang-layang: {luas_layang_layang}")
# print(f"Keliling layang-layang: {keliling_layang_layang}")


def tambah(a, b):
    return a + b

def kurang(a, b):
    return a - b

def kali(a, b):
    return a * b

def bagi(a, b):
    if b != 0:
        return a / b
    else:
        return "Error: Tidak dapat melakukan pembagian dengan nol"

def pangkat(a, b):
    return a ** b

# Input dari pengguna
angka1 = float(input("Masukkan angka pertama: "))
angka2 = float(input("Masukkan angka kedua: "))
operator = input("Pilih operator (+, -, *, /, **): ")

# Pilihan operator
if operator == '+':
    hasil = tambah(angka1, angka2)
    operator_keterangan = "Tambah"
elif operator == '-':
    hasil = kurang(angka1, angka2)
    operator_keterangan = "Kurang"
elif operator == '*':
    hasil = kali(angka1, angka2)
    operator_keterangan = "Kali"
elif operator == '/':
    hasil = bagi(angka1, angka2)
    operator_keterangan = "Bagi"
elif operator == '**':
    hasil = pangkat(angka1, angka2)
    operator_keterangan = "Pangkat"
else:
    hasil = "Error: Operator tidak valid"
    operator_keterangan = "Tidak diketahui"

# Output hasil
print(f"Angka pertama: {angka1}")
print(f"Angka kedua: {angka2}")
print(f"Pilihan Operator: {operator_keterangan}")
print(f"Hasil operator {angka1} {operator} {angka2} = {hasil}")
