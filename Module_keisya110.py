def buat(baris, kolom, nilai=0):
    return [[nilai for _ in range(kolom)] for _ in range(baris)]

def cetak(matriks):
    for baris in matriks:
        print(" ".join(map(str, baris)))

def ukuran(matriks):
    baris = len(matriks)
    kolom = len(matriks[0]) if baris > 0 else 0
    return baris, kolom

def tambah(m1, m2):
    if len(m1) != len(m2) or len(m1[0]) != len(m2[0]):
        raise ValueError("Ukuran matriks harus sama!")
    hasil = buat(len(m1), len(m1[0]))
    for i in range(len(m1)):
        for j in range(len(m1[0])):
            hasil[i][j] = m1[i][j] + m2[i][j]
    return hasil

def kurang(m1, m2):
    if ukuran(m1) != ukuran(m2):
        raise ValueError("Ukuran matriks harus sama!")
    b, k = ukuran(m1)
    hasil = buat(b,k)
    for i in range (b):
        for j in range (k):
            hasil[i][j] = m1[i][j] - m2[i][j]
    return hasil

def kali(m1, m2):
    if len(m1[0]) != len(m2):
        raise ValueError("Kolom matriks 1 harus sama dengan baris matriks 2!")
    hasil = buat(len(m1), len(m2[0]))
    for i in range(len(m1)):
        for j in range(len(m2[0])):
            for k in range(len(m2)):
                hasil[i][j] += m1[i][k] * m2[k][j]
    return hasil

def kali_skalar(matriks, skalar):
    b, k = ukuran(matriks)
    hasil = buat(b,k)
    for i in range (b):
        for j in range (k):
            hasil[i][j] =  matriks [i][j] * skalar
    return hasil

def transpose(matriks):
    b, k = ukuran(matriks)
    hasil = buat(k, b)
    for i in range(b):
        for j in range(k):
            hasil[j][i] = matriks[i][j]
    for baris in hasil:
        print(" ".join(map(str, baris)))

def ambil_submatriks(matriks, baris_diabaikan, kolom_diabaikan):
    return [
        [matriks[i][j] for j in range(len(matriks[i])) if j != kolom_diabaikan]
        for i in range(len(matriks)) if i != baris_diabaikan
    ]

def determinan(matriks):
    b, k = ukuran(matriks)
    if b != k:
        raise ValueError("Determinan hanya bisa dihitung untuk matriks persegi!")
    if b == 1:
        return matriks[0][0]
    if b == 2: 
        return (matriks[0][0] * matriks[1][1]) - (matriks[0][1] * matriks[1][0])
    total_det = 0
    for j in range(k): 
        sub = ambil_submatriks(matriks, 0, j)
        tanda = 1 if j % 2 == 0 else -1
        total_det += tanda * matriks[0][j] * determinan(sub)
    return total_det
