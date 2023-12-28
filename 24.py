from collections import Counter
# Counter('aaabb')
# -> {'a': 3, 'b': 2}

def rearrange_string(s):
    freq = Counter(s)
    freq = {k: v for k, v in sorted(freq.items(), key=lambda item: item[1], reverse=True)}

    result = ""
    while freq:
        keys = list(freq.keys())
        for key in keys:
            result += key
            freq[key] -= 1
            if freq[key] == 0:
                del freq[key]
        
    return result

# Пример использования
s = "aaabbbc"
rearranged = rearrange_string(s)
print(rearranged)  # Вывод: "abcabab"