from random import randint

def count_paths(N):
   if N <= 2:
       return N

   fib = [0]*(N+1)
   fib[1] = 1
   fib[2] = 2

   for i in range(3, N+1):
       fib[i] = fib[i-1] + fib[i-2] + fib[i-3]

   return fib[N]

