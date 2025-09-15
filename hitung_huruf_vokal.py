# program hitung huruf vokal

kalimat = input("masukkan kalimat: ").lower()

huruf_vokal = ['a','i','u','e','o']

counter = 0

for x in list(kalimat):
    if x in huruf_vokal:
        counter += 1

print("jumlah huruf vokal:",counter)
