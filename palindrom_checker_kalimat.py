# program palindrom checker kalimat

kalimat = input("masukkan kalimat: ")

if kalimat == kalimat[::-1]:
    print(kalimat,"adalah palindrome")
else:
    print(kalimat,"bukan palindrome")
