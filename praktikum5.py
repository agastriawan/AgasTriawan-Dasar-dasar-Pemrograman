list_kendaraan = ["Nama Kendaraan", "Jenis Kendaraan", "cc Kendaraan", "Warna Kendaraan", "Roda Kendaraan"]

list_kendaraan.append("Harga Kendaraan")
list_kendaraan.append("Tipe Kendaraan")
list_kendaraan.insert(2, "Merk Kendaraan")

print(list_kendaraan)

luas_bangunan_datar = int(input("Masukan Jenis Bangunan Datar: "))

match luas_bangunan_datar:
    case 1:
        print("Menghitung Luas Persegi (s x s)")
        sisi1 = float(input("Masukkan sisi : "))
        sisi2 = float(input("Masukkan sisi : "))
        luas_persegi = sisi1 * sisi2
        print("Hasilnya adalah", luas_persegi)
    case 2:
        print("Menghitung Luas Lingkaran (3.14 x r x r)")
        phi = 3.14
        r = float(input("Jari - jari : "))
        luas_lingkaran = phi * r * r
        print("Hasilnya adalah", luas_lingkaran)
    case 3:
        print("Menghitung Luas Segitiga (0.5 x a x t)")
        setengah = 0.5
        a = float(input("Alas : "))
        t = float(input("Tinggi : "))
        luas_segitiga = setengah * a * t
        print("Hasilnya adalah", luas_segitiga)
    case _:
        print("Salah Pilih Angka")
    
        



