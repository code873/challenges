# program tebak angka

import random

m = random.randint(1,100)

count = 1
while count<=7:
    n = int(input("masukkan angka antara 1-100: "))
    if n < m:
        print("angka terlalu kecil")
        if count == 6:
            print("SAYANG SEKALI !!, tebakanmu tidak ada yang tepat..")
            print("game selesai..")
            break
    elif n > m:
        print("angka terlalu besar")
        if count == 6:
            print("SAYANG SEKALI !!, tebakanmu tidak ada yang tepat..")
            print("game selesai..")
            break
    else:
        print("SELAMAT !!, tebakanmu tepat..")
        print("game selesai..")
        break
    count += 1
