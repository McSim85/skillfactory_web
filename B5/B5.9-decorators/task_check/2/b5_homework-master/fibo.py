def fibo(N):
    a = 1
    b = 2
    n = 0
    f = [1,2]
    while True:
        n = a + b
        if n > N:
            break
        else:
            f.append(n)
            a = b
            b = n
    return f

if __name__ == "__main__":

    summ = 0
    f = fibo(4000000)
    print(f[-1])
    for i in f:
        if i %2 == 0:
            summ += i
    print(summ)