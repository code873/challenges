# program cek palindrome

text = input("masukkan kata: ")
l = list(text)

if len(text)%2 == 0: # karakter genap
    x = l[:int(len(l)/2)]
    y = l[int(len(l)/2):]
    print(f"{x} adalah {int(len(l)/2)} karakter pertama")
    print(f"{y} adalah {int(len(l)/2)} karakter terakhir")
    y.reverse()
    print(f"{y} adalah {int(len(l)/2)} karakter terakhir setelah di-reverse")
    if x == y:
        print(text,"adalah palindrome")
    else:
        print(text,"bukan palindrome")

else:
    x = l[:int(len(l)/2)]
    y = l[int(1+len(l)/2):]
    print(f"{x} adalah {int(len(l)/2)} karakter pertama")
    print(f"{y} adalah {int(len(l)/2)} karakter terakhir")
    y.reverse()
    print(f"{y} adalah {int(len(l)/2)} karakter terakhir setelah di-reverse")
    if x == y:
        print(text,"adalah palindrome")
    else:
        print(text,"bukan palindrome")

