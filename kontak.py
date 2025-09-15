# program daftar kontak

#import subprocess   # buat bisa kasih perintah ke terminal

# fungsi
class database:
    nama = ""
    nomor = ""
    def __init__(self, nama, nomor):
        self.na = nama
        self.no = nomor
    def save(self):
        with open('dataKontak.txt','a') as W:
            W.write(f"{self.na} -- {self.no}\n")
    def display(self):
        with open('dataKontak.txt','r') as R:
            print("-----------------------------")
            print("++ DAFTAR KONTAK TERSIMPAN ++")
            print("-----------------------------")
            for i in R:
                print(i.strip())
            print("-----------------------------")

# objek
options = ["Tambah Kontak","Lihat Kontak","Cari Kontak"]
for i in range(len(options)):
    print(i+1,".",options[i])
choose = int(input("Pilih mana (masukkan index)? "))
if choose == 1:
    nama = input("Nama: ")
    nomor = input("Nomor: ")
    data = database(nama,nomor)
    data.save()
    data.display()
elif choose == 2:
    data = database("","")
    data.display()
elif choose == 3:
    cari = input("Masukkan nama/nomor yang akan dicari: ")
    print("--- OUTPUT :")

#    cara 2: pakai modul subprocess, tapi melibatkan 'grep'
#    Kelemahan 'grep': perintah ini hanya bisa dijalankan di linux & macOS, di windows akan gagal
#    Makanya aku pake pythonic..
#    subprocess.run([
#        'grep',cari.upper(),'dataKontak.txt'
#    ]).stdout

# pakai Pythonic dengan cara:
# buka dulu file 'dataKontak.txt', lalu loop semua line sambi cari
# kata nya.
    with open('dataKontak.txt','r') as R:
        found = False   # inisiasi misal belum ketemu yg dicari
        for line in R:
            if cari.lower() in line.lower(): # jika yang dicari ada di dalam file
                found = True    # tanda yang dicari sudah ketemu
                print(line.strip()) # tampilkan line tersebut
        if not found:   # artinya if found == False
            print("Kontak tidak ditemukan..")
