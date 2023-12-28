from random import randint
arr1 = sorted([randint(1, 99) for _ in range(randint(1, 10))])
arr2 = sorted([randint(1, 99) for _ in range(randint(1, 10))])

merged = []
i = j = 0

while i < len(arr1) and j < len(arr2):
    if arr1[i] <= arr2[j]:
        merged.append(arr1[i])
        i += 1
    else:
        merged.append(arr2[j])
        j += 1

merged.extend(arr1[i:])
merged.extend(arr2[j:])

print(merged)