# program hitung kata dalam kalimat

kalimat = input("masukkan kalimat: ").split()
# dgn adanya split, kalimat udah otomatis menjadi list.
# split() tidak diisi argumen agar menghindari spasi ganda dari user.
# karena spasi ganda bisa dihitung anggota ' ' di dalam list.

print("Jumlah kata dalam kalimat tersebut adalah",len(kalimat))
