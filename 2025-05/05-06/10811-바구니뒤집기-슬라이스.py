N, M = map(int, input().split())
basket = [i for i in range(1, N+1)]

for _ in range(M):
    i, j = map(int, input().split())

    basket[i-1:j] = basket[i-1:j][::-1]

print(*basket)

# 리스트[start:stop] -> 끝 인덱스는 불포함
# [::-1] -> 뒤집기(역순)

# arr = [1, 2, 3, 4, 5]
# arr[1:4] = [100, 200, 300]
# print(arr)  # [1, 100, 200, 300, 5]

# 이런식으로 바꿔도 됨됨