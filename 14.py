def galopping(AB, n, C):
    C[:] = AB[:n]

    # r - укзатель на конец результата
    # j - место последней вставки
    # m - длина остатка B
    
    r, j, m = 0, n, len(AB) - n
    
    for i in range(n):
        # k - степень двойки
        # l - указатель на 2**k - 1
        k, l = 0, 0

        while l < m and AB[j+1] < C[i]:
            k += 1
            l = 2**k - 1
        
        if l >= m:
            l = m-1

        while l >= 0 and AB[j+1] > C[i]:
            l -= 1
        
        l += 1
        AB[r:r+1], AB[r+1] = AB[j:j+1], C[i]
        r, j, m = r+l+1, j+l, m-l