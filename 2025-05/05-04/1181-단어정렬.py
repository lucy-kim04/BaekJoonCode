n = int(input())
words = [input() for _ in range(n)]

unique_words = list(set(words))  # 중복 제거

# 정렬: (길이(len), 알파벳 순(sort))
unique_words.sort(key=lambda x: (len(x), x))

for word in unique_words:
    print(word)
