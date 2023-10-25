list_kendaraan = ["Mobil", "Super Car", 1998, "Kuning", 4]

list_kendaraan.append("$2000")
list_kendaraan.append("M1")
list_kendaraan.insert(2, "BMW")

print(list_kendaraan)

luas_bangunan_datar = int(input("Masukan Jenis Bangunan Datar: "))

match luas_bangunan_datar:
    case 1:
        print("Menghitung Luas Persegi (s x s)")
        sisi = float(input("Masukkan sisi : "))
        luas_persegi = sisi * sisi
        print("Hasilnya adalah", int(luas_persegi))
    case 2:
        print("Menghitung Luas Lingkaran (3.14 x r x r)")
        phi = 3.14
        r = float(input("Jari - jari : "))
        luas_lingkaran = phi * r * r
        print("Hasilnya adalah", int(luas_lingkaran))
    case 3:
        print("Menghitung Luas Segitiga (0.5 x a x t)")
        setengah = 0.5
        a = float(input("Alas : "))
        t = float(input("Tinggi : "))
        luas_segitiga = setengah * a * t
        print("Hasilnya adalah", int(luas_segitiga))
    case _:
        print("Salah Pilih Angka")
    
        



