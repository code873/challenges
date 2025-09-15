# program fibonacci sequence

print("-- Program n Fibonacci Sequence --")

n = int(input("masukkan (n>0): "))

if n == 1:
    print("Barisan",n,"Fibonacci: 0")

elif n == 2:
    print("Barisan",n,"Fibonacci: 0 1")

else:
    for i in range(n-2):
        fib.append(fib[i]+fib[i+1])
    print("Barisan",n,"Fibonacci:",*fib)
