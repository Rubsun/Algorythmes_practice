def euclidus(n, m):
    while n % m > 0:
        m, n = n, m % n
    return n