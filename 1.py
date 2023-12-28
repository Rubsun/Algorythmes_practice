a, b, c = int(input()), int(input()), int(input())
summ = a + b
ans = []
while summ != 0:
    ans.append(summ % c)
    summ = summ // c
print([ans[i] for i in range(len(ans)-1, -1, -1)])