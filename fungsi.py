def greeting(nama, pesan):
    return "Halo, " + nama + "! " + pesan

print(greeting("Dicoding", "Selamat pagi!"))
print(greeting(pesan="Selamat sore!", nama="Dicoding"))

def mencari_luas_persegi_panjang(panjang,lebar):
    luas_persegi_panjang = panjang*lebar
    return luas_persegi_panjang

persegi_panjang_pertama = mencari_luas_persegi_panjang(panjang=5, lebar=10)

print(persegi_panjang_pertama)


def mencari_luas_persegi_panjang(panjang,lebar):
    luas_persegi_panjang = panjang*lebar
    return luas_persegi_panjang

persegi_panjang_pertama = mencari_luas_persegi_panjang(5,10)
print(persegi_panjang_pertama)

def mencari_luas_persegi_panjang(panjang,lebar): #ini untuk mencari luas persegi panjang
    """
    Fungsi ini digunakan untuk menghitung luas persegi panjang.

    Args:
        panjang (int): Panjang persegi panjang.
        lebar (int): Lebar persegi panjang.

    Returns:
        int: Luas persegi panjang hasil perhitungan.
    """

    luas_persegi_panjang = panjang*lebar
    return luas_persegi_panjang

persegi_panjang_pertama = mencari_luas_persegi_panjang(5,10)
print(persegi_panjang_pertama)
persegi_panjang_kedua = mencari_luas_persegi_panjang(12,5)
print(type(persegi_panjang_kedua))

def mencari_luas_persegi_panjang(panjang,lebar):
    luas_persegi_panjang = panjang*lebar
    return luas_persegi_panjang

persegi_panjang_pertama = mencari_luas_persegi_panjang(panjang=5, lebar=10)

print(persegi_panjang_pertama)


# Positional-or-Keyword
def greeting(nama, pesan):
    return "Halo, " + nama + "! " + pesan

print(greeting("Dicoding", "Selamat pagi!"))
print(greeting(pesan="Selamat sore!", nama="Dicoding"))

#Positional-Only
def penjumlahan(a, b, /): #mendefinisikan parameter fungsi dengan sintaks "/".
    return a + b

print(penjumlahan(8, 50))

# print(penjumlahan(a=3, b=5))

#Keyword-Only
def greeting(*, nama, pesan): #argument untuk memanggil fungsi dengan jenis parameter ini. Ia ditentukan dengan sintaks "*" (asterisk)
    return "Halo, " + nama + "! " + pesan

print(greeting(pesan="Selamat sore!",nama="Dicoding"))


#Var-Positional (Variadic Positional Parameter)
def hitung_total(*args): #*args mengumpulkan semua argumen posisi yang diberikan saat pemanggilan fungsi dan membungkusnya menjadi tuple "args"
    print(type(args))
    total = sum(args)
    return total

print(hitung_total(1, 2, 3))

#Var-Keyword (Variadic Keyword Parameter)
'''**kwargs yang berperan sebagai dictionary (seperti tipe datanya). 
Argumen pada pemanggil fungsi akan berperan sebagai value dan parameter (identifier) berperan sebagai key.'''
def cetak_info(**kwargs): 
    info = ""
    for key, value in kwargs.items():
        info += key + ': ' + value + ", "
    return info

print(cetak_info(nama="Dicoding", usia="17", pekerjaan="Python Programmer"))

mencari_luas_persegi_panjang = lambda panjang, lebar: panjang*lebar
print(mencari_luas_persegi_panjang(5,10))

def minimal(a,b,/):
  return a <= b
print(minimal(2,5))
