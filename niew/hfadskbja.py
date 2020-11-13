def fib_iter2(n):
    a, b = 0, 1
    print("wyraz", 1, a)
    print("wyraz", 2, b)
    for i in range(1, n - 1):
         wynik = a + b
        a, b = b, a + b
        print("wyraz", i + 2, b)

    print()  
    return b
