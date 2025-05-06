N, M = map(int, input().split())
basket = []
for i in range(1, N+1):
    basket.append(i)

for _ in range(M):
    i, j = map(int, input().split())
    # 인덱스 맞추기 위해 -1
    basket[i-1], basket[j-1] = basket[j-1], basket[i-1]  # swap

print(*basket)
