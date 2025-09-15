# program bilangan prima

from time import sleep

n = int(input("masukkan bilangan: "))

count = 2

while (count<n):
    print(n,"%",count,"=",n%count)
    sleep(0.5)
    if n%count == 0:
        print(f"{n} bukan bilangan prima")
        sleep(1)
        break
    else:
        if count == n-1:
            print(f"{n} adalah bilangan prima")
            sleep(1)
    count += 1
