# program tebak angka

import random

choose = 'y'
round_count = 1

while choose.lower() == 'y':
    print("-- Program Tebak Angka --")
    angka_komputer = random.randint(1,100)
    print("Masukkan angka tebakanmu (n), kamu punya 7 kali kesempatan")
    print(f"Round {round_count}")
    for i in range(7):
        angka_user = int(input(f"Tebakan ke-{i+1} --> n: "))
        if angka_user < angka_komputer:
            print("> Angkamu terlalu kecil")
        elif angka_user > angka_komputer:
            print("> Angkamu terlalu besar")
        else:
            print("> SELAMAT !!, tebakanmu benar")
            print("Game selesai..")
            break
    else:
        print("> SAYANG SEKALI !!, tebakanmu salah semua")
        print("Game selesai..")

    choose = input("# Mau coba lagi (y/t): ")

    round_count += 1
