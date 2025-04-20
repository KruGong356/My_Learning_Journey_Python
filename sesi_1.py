


def menghitung_persegi_panjang(p : float, l : float) -> None:
    hasil = p*l
    print(hasil)

def menghitung_segitiga(alas: float, tinggi: float) -> int:
    hasil = 0.5 * alas * tinggi
    print(hasil)
    return int(hasil)

x, y = map(int, input('input panjang dan lebar : ').split())
hasil = menghitung_segitiga(x, y)

print('hasil diluar fungsi : ', hasil)

menghitung_persegi_panjang(x, hasil)