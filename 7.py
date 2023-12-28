def eratosphene(n):
    sieve = [True] * (n+1)
    sieve[0] = sieve[1] = False

    for i in range(2, int(n**0.5)+2):
        if sieve[i] == True:
            for j in range(i*i, n+1, i):
                sieve[j] = False

    return sum(sieve)
print(eratosphene(300))