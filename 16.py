def lcs(X, Y):
    m = len(X)
    n = len(Y)

    # Создаем таблицу
    LCS = [[0]*(n+1) for _ in range(m+1)]

    # Заполняем таблицу
    for i in range(m+1):
        for j in range(n+1):
            if i == 0 or j == 0:
                LCS[i][j] = 0
            elif X[i-1] == Y[j-1]:
                LCS[i][j] = LCS[i-1][j-1] + 1
            else:
                LCS[i][j] = max(LCS[i-1][j], LCS[i][j-1])
    for i in LCS:
        print(*i)
    return LCS[m][n]

x, y = 'abcdefg', 'bcdefgh'
print(lcs(x, y))