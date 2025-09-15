# program kalkulator matriks 2x2

import numpy as np

def kal_matriks(obj1,obj2):
    yield obj1+obj2
    yield obj1-obj2
    yield np.dot(obj1,obj2)

print("-- Kalkulator Matriks 2x2 -- ")
print("Inputkan bilangan-bilangan yang menyusun matriks: a_11, a_12, a_21, a_22")

# list kosong untuk menampung inputan user berupa list 2 dimensi
matriks1 = []
matriks2 = []

# input user masih berupa string
m1 = input("Matriks pertama: ").split(",")
m2 = input("Matriks kedua: ").split(",")

# append inputan user ke matriks1 dan matriks2
for i in range(0,3,2):
    matriks1.append([m1[i],m1[i+1]])
    matriks2.append([m2[i],m2[i+1]])

# konversi ke array 2x2 sekaligus mengubah type menjadi integer
Matrix1 = np.array([[int(x) for x in matriks1[0]]] + [[int(x) for x in matriks1[1]]])
Matrix2 = np.array([[int(x) for x in matriks2[0]]] + [[int(x) for x in matriks2[1]]])

# list operasi
operasi = ["Jumlah","Kurang","Kali"]

# buat generator
gen = kal_matriks(Matrix1,Matrix2)

for j in range(3):
    print(operasi[j],":")
    print(next(gen))

