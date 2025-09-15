# program batu gunting kertas
import random

def bgk():
    global skor_komputer
    global skor_kamu
    kamus = {1:"BATU", 2:"GUNTING", 3:"KERTAS"}
    objek = [1,2,3]
    round_count = 1
    while (round_count<=3):
        print(f"Round {round_count}")
        komputer = random.choice(objek)
        print("Pilih salah satu:")
        for i in range(3):
            print(i+1,".",kamus[i+1])
        print("Masukkan nomor index nya saja ..\n")
        try:
            user = int(input(">> "))
            # SERI
            if user == komputer:
                print(f"Kamu & Komputer memilih objek yang sama, yaitu {kamus[komputer]}\n")
                skor_komputer += 0.5
                skor_kamu += 0.5
                round_count += 1
                continue
            # TIDAK SERI
            else:
                if user == 1 and komputer == 2:
                    print(f"Kamu {kamus[1]} & Komputer {kamus[2]}")
                    print("> Kamu Menang\n")
                    skor_kamu += 1
                elif user == 2 and komputer == 1:
                    print(f"Kamu {kamus[2]} & Komputer {kamus[1]}")
                    print("> Komputer Menang\n")
                    skor_komputer += 1
                elif user == 1 and komputer == 3:
                    print(f"Kamu {kamus[1]} & Komputer {kamus[3]}")
                    print("> Komputer Menang\n")
                    skor_komputer += 1
                elif user == 3 and komputer == 1:
                    print(f"Kamu {kamus[3]} & Komputer {kamus[1]}")
                    print("> Kamu Menang\n")
                    skor_kamu += 1
                elif user == 2 and komputer == 3:
                    print(f"Kamu {kamus[2]} & Komputer {kamus[3]}")
                    print("> Kamu Menang\n")
                    skor_kamu += 1
                elif user == 3 and komputer == 2:
                    print(f"Kamu {kamus[3]} & Komputer {kamus[2]}")
                    print("> Komputer Menang\n")
                    skor_komputer += 1
        except ValueError:
            print("\nInputmu salah.. coba lagi\n")
        round_count += 1

def decision():
    print("Total skor Komputer :",skor_komputer)
    print("Total skor Kamu :",skor_kamu)
    if skor_komputer > skor_kamu:
        print("Komputer Menang !")
    elif skor_komputer < skor_kamu:
        print("Kamu Menang !")
    else:
        print("Skor kalian imbang")

while True: # loop yang tidak pernah berhenti
    skor_komputer = 0
    skor_kamu = 0
    bgk()
    decision()
    choose = input("\nMau coba main lagi (y/t): ")
    if choose.lower() != 'y':   # kondisi false yang akan menghentikan loop
        break
