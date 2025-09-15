# program anagram checker

n = input("masukkan kata1: ")
m = input("masukkan kata2: ")

if set(n) == set(m):
    print(n,"dan",m,"adalah anagram")
else:
    print(n,"dan",m,"bukan anagram")
