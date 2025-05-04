S = input()
result = [-1] * 26

for i in range(len(S)):
    ch = S[i]
    idx = ord(ch) - ord('a') 

    if result[idx] == -1:
        result[idx] = i

print(' '.join(map(str, result)))
