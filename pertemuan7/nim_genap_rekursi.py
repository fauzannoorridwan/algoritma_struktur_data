# PROGRAM NIM GENAP
def fibonacci(n):
    if n <= 1:
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2)

def kali(m, n):
    if n == 1:
        return m
    return m + kali(m, n - 1)
def menu():
    print("\nNim Genap")
    print("menu pilihan")
    print("1. Barisan Fibonacci")
    print("2. M Kali N")
    print("0. Keluar")
while True:
    menu()
    pilihan = input("Pilih Menu : ")

    if pilihan == "1":
        n = int(input("Masukkan Jumlah Suku : "))
        hasil = [fibonacci(i) for i in range(n)]
        print(f"barisan fibonacci sebanyak {n} suku :")
        print(", ".join(map(str, hasil)))

    elif pilihan == "2":
        m = int(input("Masukkan Suatu Bilangan Bulat : "))
        n = int(input("Masukkan Suatu Bilangan Pengali : "))
        print(f"Hasil {m} x {n} = {kali(m, n)}")

    elif pilihan == "0":
        print("Keluar dari program.")
        break
