def min_sum(arr):
   arr.sort()
   num1 = ''
   num2 = ''
   for i in range(len(arr)):
       if i % 2 == 0:
           num1 += str(arr[i])
       else:
           num2 += str(arr[i])
   return int(num1) + int(num2)

print(min_sum([6, 8, 4, 5, 2, 3])) # Output: 604
print(min_sum([5, 3, 0, 7, 4])) # Output: 82