n = int(input("Masukkan n: "))
suku1 = 0
suku2 = 0
fibo = 1
i = 1
while (i <= n):
        print(fibo)
        suku1 = suku2
        suku2 = fibo
        fibo = suku1 + suku2
        i += 1
        print(fibo,end ='')
        