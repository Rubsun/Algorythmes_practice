from random import randint
N = 6
a = [randint(1, 99) for _ in range(N)]

for i in range(N-1):
    for j in range(N-i-1):
        if a[j] > a[j+1]:
            a[j], a[j+1] = a[j+1], a[j]

print(a)