import math

def tambah(bil1, bil2):
    hasil = bil1 + bil2
    print("hasil tambah dari", bil1, "+", bil2, "=", hasil)

def kurang(bil1, bil2):
    hasil = bil1 - bil2
    print("hasil pengurangan dari", bil1, "-", bil2, "=", hasil)

def kali(bil1, bil2):
    hasil = bil1 * bil2
    print("hasil perkalian dari", bil1, "*", bil2, "=", hasil)

def bagi(bil1, bil2):
    hasil = bil1 / bil2
    print("hasil pembagian dari", bil1, "/", bil2, "=", hasil)

def pangkat(bil1, bil2):
    hasil = math.pow(bil1, bil2)
    print("hasil pemangkatan dari", bil1, "^", bil2, "=", hasil)

def logaritma(bil):
    hasil = math.log(bil)
    print("hasil logaritma dari", bil, "=", hasil)

def akar(bil):
    hasil = math.sqrt(bil)
    print("hasil akar kuadrat dari", bil, "=", hasil)

def sin(nilai):
    hasil = math.sin(math.radians(nilai))
    print("hasil sin dari", nilai, "=", hasil)

def cos(nilai):
    hasil = math.cos(math.radians(nilai)) 
    print("hasil cos dari", nilai, "=", hasil)

def tan(nilai):
    hasil = math.tan(math.radians(nilai))
    print("hasil tan dari", nilai, "=", hasil)

