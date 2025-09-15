text = input("masukkan kata: ")

if text == text[::-1]: #membuat salinan string dari belakang ke depan:
    print(text,"adalah palindrome")
else:
    print(text,"bukan palindrome")
