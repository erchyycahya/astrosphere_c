def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)


def main():
    # Minta input dari pengguna
    n = int(input("Masukkan batas deret Fibonacci: "))

    # Cetak deret Fibonacci
    print("Deret Fibonacci hingga batas", n, "adalah:")
    for i in range(n):
        print(fibonacci(i))


if _name_ == "_main_":
    main()