# program faktorial
# pakai fungsi rekursif

def faktorial(n):
    if n == 0:
        return 1
    elif n == 1:
        return 1
    else:
        return n*faktorial(n-1)

n = int(input("masukkan bilangan: "))
print(faktorial(n))
