def divisor(a):
    for i in range(1, a):
        if a % i == 0:
            print(i)

divisor(100)