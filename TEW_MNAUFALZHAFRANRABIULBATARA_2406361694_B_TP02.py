while True: #akan loop sampai user memasukkan nama file yang tepat
    try:
        nama_file = input("Genome file name: ")
        open_file = open(nama_file, "r") #memilih mode read untuk file yang diinput
        genome = open_file.read()   #membaca isi file
        break
    except FileNotFoundError: 
        print("File tidak ditemukan")

def reverse_pattern(strand):  #fungsi untuk mengubah strand menjadi complementary strand
    global complement #membuat  variabel global agar bisa diakses di fungsi lain
    complement = ""
    huruf = ['A',  'C', 'G', 'T']

    for i in range(len(strand)):  #mengubah setiap huruf pada strand menjadi huruf yang sesuai pada complementary strand
        if strand[i] == "A":
            complement += "T"
        elif strand[i] == "T":
            complement += "A"
        elif strand[i] == "C":
            complement += "G"
        elif strand[i] == "G":
            complement += "C"
        if  strand[i] not in huruf:
            complement =  "Invalid DNA strand" 
            break
    
def count_k_mer(pattern):   #fungsi untuk menghitung k-mer pada genome
    count = 0
    reverse_pattern(pattern)  #memanggil  fungsi reverse_pattern untuk mengubah pattern menjadi complementary strand
    reverse = complement[::-1]
    for i in range(len(genome) - len(pattern) + 1): #mengecek semua kemungkinan  k-mer pada genome
        if genome[i:i+len(pattern)] == pattern:  #jika k-mer cocok dengan pattern maka jumlah + 1
            count += 1
        if genome[i:i+len(pattern)] == reverse:   #jika k-mer cocok dengan complementary strand maka jumlah + 1
            count += 1
    
    if complement == 'Invalid DNA strand':
        print(complement)
    else:
        print(count)

def frequent_k_mer(k):   #fungsi untuk mencari k-mer yang paling sering muncul pada genome
    k_mer_list = []
    for i in range(len(genome) - k+1): #mengecek semua kemungkinan  k-mer pada genome
        k_mer = genome[i:i+k]    
        k_mer_list.append(k_mer)
    
    k_mer = []
    count = []
    for i in k_mer_list: #menghitung jumlah k-mer  yang sama
        if i not in k_mer:
            k_mer.append(i)
            jumlah = 0
            for j in k_mer_list:  
                if i == j:
                    jumlah += 1
            count.append(jumlah)

    hapus = []
    comple = []
    for i in range(len(k_mer)): #mengubah k-mer menjadi complement
        reverse_pattern(k_mer[i])   #memanggil  fungsi reverse_pattern untuk mengubah k-mer menjadi complementary strand
        reverse = complement[::-1] 
        for l in range(len(k_mer)): #menggabung k-mer dan complementarynya
            if k_mer[i] in comple: #jika complementarynya sudah di cek  maka tidak perlu di cek lagi
                break
            if k_mer[l] not in comple:
                if k_mer[l] == reverse:
                    count[i] += count[l] #menggabung jumlah k-mer dengan complementnya
                    hapus.append(l)  #menyimpan indeks yang akan di hapus
                    comple.append(reverse)  #menyimpan k-mer yang sudah di cek
                    break
                else:
                    continue
    hapus.sort()  #mengurutkan indeks yang akan di hapus
    for i in hapus[::-1]: #menghapus dari yang besar agar tidak terjadi kesalahan indeks saat menghapus
        k_mer.pop(i)
        count.pop(i)

    most_frequent = count[0]
    index = 0
    for k in range(len(count)):  #mencari k-mer yang paling sering muncul
        if count[k] > most_frequent:
            most_frequent = count[k]
            index = k

    most = []
    index2 = 0
    for j in range(len(count)): #mengecek jika ada jumlah k-mer yang sama
        if count[j] == most_frequent and j != index:
            index2 = j
            most.append(k_mer[index2])
            reverse_pattern(k_mer[index2])
            most.append(complement[::-1])
        elif count[j] != most_frequent:
            continue
            
    most.append(k_mer[index])
    reverse_pattern(k_mer[index])
    most.append(complement[::-1])
    for i in most: #mencetak k-mer yang paling sering muncul
        print(i)
    
def main():  #fungsi utama
    while True:
        print("""Choose an option: 
[1] Compute a reverse complement of a k-mer pattern      
[2] Count a k-mer pattern
[3] Find most frequent k-mer patterns
[4] Quit    """)                                      #mencetak pilihan menu

        operation = int(input("\nSelect an operation [1/2/3/4]: "))

        if operation == 1:  #jika pilihan 1 maka akan mencetak reverse complement

            while True:
                reverse_pattern(input("Input your pattern: ").upper())
                if complement  == "Invalid DNA strand":
                    print(complement)
                else:
                    print(complement[::-1])
                while True:
                    lanjut =  input("Do you want to continue? [y/n]: ").lower()  #mengulang input hingga user memilih untuk berhenti
                    if lanjut == 'y':
                        break
                    elif lanjut == 'n':
                        break
                    else:
                        print("Invalid input. Please try again.")
                        continue
                if lanjut == 'y':
                    continue
                elif lanjut == 'n':
                    break

        elif operation == 2:   #jika pilihan 2 maka akan menghitung k-mer
            while  True:
                count_k_mer(input("Input your pattern: ").upper())
                while  True:
                    lanjut =  input("Do you want to continue? [y/n]: ").lower()   #mengulang input hingga user memilih untuk berhenti
                    if lanjut == 'y':
                        break
                    elif lanjut == 'n':
                        break
                    else:
                        print("Invalid input. Please try again.")
                        continue
                if lanjut == 'y':
                    continue
                elif lanjut == 'n':
                    break
                
        elif operation == 3:   #jika pilihan 3 maka akan mencari k-mer yang paling sering muncul
            while True:
                while True:
                    try:
                        frequent_k_mer(int(input("Input your value of k: "))) #memastikan k adalah angka
                        break
                    except  ValueError:
                        print("Invalid input. Please try again.")
                while True:
                    lanjut =  input("Do you want to continue? [y/n]: ").lower()    #mengulang input hingga user memilih untuk berhenti
                    if lanjut == 'y':
                        break
                    elif lanjut == 'n':
                        break
                    else:
                        print("Invalid input. Please try again.")
                        continue
                if lanjut == 'y':
                    continue
                elif lanjut == 'n':
                    break

        elif operation == 4:    #jika pilihan 4 maka akan keluar dari program
            open_file.close()   #menutup file yang telah dibuka
            print("See you later! ")
            break
        else: #jika user meinginput pilihan yang tidak ada di menu
            print("Invalid input. Please try again.") 

if __name__  == "__main__":
    main()   #memanggil fungsi main() untuk menjalankan program
