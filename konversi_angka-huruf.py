# program konversi angka ke huruf

numb = input("masukkan angka: ")

n = list(numb)

satuan = {'1':'satu','2':'dua','3':'tiga','4':'empat','5':'lima',
            '6':'enam','7':'tujuh','8':'delapan','9':'sembilan'}
puluhan_satuan = {'10':'sepuluh','11':'sebelas','12':'dua belas',
        '13':'tiga belas','14':'empat belas','15':'lima belas',
        '16':'enam belas','17':'tujuh belas','18':'delapan belas',
        '19':'sembilan belas'}
puluhan2 = {'2':'dua puluh','3':'tiga puluh','4':'empat puluh',
            '5':'lima puluh','6':'enam puluh','7':'tujuh puluh',
                '8':'delapan puluh','9':'sembilan ratus'}
ratusan = {'1':'seratus','2':'dua ratus','3':'tiga ratus',
                '4':'empat ratus','5':'lima ratus',
        '6':'enam ratus','7':'tujuh ratus','8':'delapan ratus',
        '9':'sembilan ratus'}

if n[1] != '1':
    print(f"{ratusan[n[0]]} {puluhan2[n[1]]} {satuan[n[2]]}")
else:
    n[1] = n[1]+n[2]
    del n[2]
    print(f"{ratusan[n[0]]} {puluhan_satuan[n[1]]}")



