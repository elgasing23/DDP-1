
def ukuran_matriks(): #function  untuk menginput ukuran matriks dan isinya
    global baris1, baris2, m, n #membuat variabel bisa digunakan diluar function
    while True:  #looping untuk memastikan input ukuran matriks benar
        ukuran = input("Masukkan ukuran matriks A dan B (m n):\n") 
        matriks = ukuran.split(' ') #memisahkan  input ukuran matriks menjadi dua 
        for i in matriks: #looping untuk mengecek apakah input valid atau tidak
            if int(i) <0:
                print("Ukuran matriks harus berupa bilangan positif")
                keluar = False
                break
            if i.isalpha():
                print("Input tidak valid. Ukuran matriks harus berupa angka")
                keluar = False
                break
            if i == 0:
                print("Input tidak valid. Ukuran matriks tidak boleh 0")
                keluar = False
                break
            if len(matriks) == 1:
                print("Input tidak valid. Ukuran harus berupa dua angka")
                keluar = False
                break
            elif len(matriks) > 2:
                print("Input tidak valid. Ukuran harus berupa dua angka")
                keluar = False
                break
            keluar = True
        if  keluar ==  True:
            break
        if keluar == False: 
            continue

    m = matriks[0] #baris matriks
    n = matriks[1] #kolom matriks

    print(f"Masukkan matriks berukuran {m}x{n}:")
    baris1 = []
    for i in range(int(m)): #meminta input matriks pertama (A)
        isi = input(f'Masukkan baris {i+1} (pisahkan dengan spasi):\n')
        isi = isi.split(' ')
        baris1.append(isi)

    print(f"\nMasukkan matriks berukuran {m}x{n}:")
    baris2 = []
    for i in range(int(m)): #meminta input matriks kedua (B)
        isi = input(f'Masukkan baris {i+1} (pisahkan dengan spasi):\n')
        isi = isi.split(' ')
        baris2.append(isi)
    
    


def penjumlahan():  #function untuk melakukan penjumlahan matriks
    global hasil
    hasil = []
    for i in range(int(m)):   #looping untuk memproses setiap baris matriks
        baris_hasil = []      #inisialisasi list kosong untuk menyimpan hasil baris
        hasil.append(baris_hasil)   #menambahkan baris hasil ke dalam hasil sebagai baris i dalam matriks baru
        for j in range(int(n)):    
            jumlah = int(baris1[i][j]) + int(baris2[i][j]) #menjumlahkan setiap elemen sesuai baris dan kolom
            baris_hasil.append(jumlah)  #menambahkan hasil penjumlahan ke dalam baris hasil


    print("\nHasil penjumlahan A + B adalah: ")
    for i in hasil:   #looping untuk menampilkan hasil matriks (agar bersusun kebawah)
        print(i)
    
    
    
def nilai_maks():
    nilai = [max(baris) for baris in hasil]  #mengambil  nilai maksimum dari setiap baris hasil
    print(f'\nList nilai maksimum dari setiap baris: {nilai}') 
    nilai.sort(reverse=True)  #mengurutkan  nilai dari besar ke kecil
    print(f'Nilai maksimum yang diurutkan dari yang tertinggi: {nilai}')


def trace():   #function untuk mencari nilai diagonal matriks
    if m != n:   #jika matriks bukan persegi, maka tidak ada diagonal
        print("Trace tidak bisa dihitung karena matriks bukan persegi. ")
    elif m == n:
        trace = 0
        for i in range(len(hasil)):
            trace += hasil[i][i]  #menjumlah elemen pada diagonal utama
        print(f"\nTrace dari matriks hasil adalah: {trace}")


    




def main(): #fungsi main
    ukuran_matriks()
    penjumlahan()
    nilai_maks()
    trace()

if __name__ ==  "__main__":  #untuk menjalankan fungsi main

    main()
        

    

