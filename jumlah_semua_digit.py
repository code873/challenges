# program jumlah semua digit dari suatu bilangan

n = input("masukkan bilangan: ")

m = [int(x) for x in list(n)]

print("Jumlah semua digit:",sum(m))
