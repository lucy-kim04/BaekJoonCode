INF = int(1e9)

n, m = map(int, input().split())
dist = [[INF] * (n + 1) for _ in range(n + 1)]

# 자기 자신은 0
for i in range(1, n + 1):
    dist[i][i] = 0

# 친구 관계는 거리 1
for _ in range(m):
    a, b = map(int, input().split())
    dist[a][b] = 1
    dist[b][a] = 1

# 플로이드 워셜
for k in range(1, n + 1):
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            if dist[i][j] > dist[i][k] + dist[k][j]:
                dist[i][j] = dist[i][k] + dist[k][j]

# 케빈 베이컨 수 계산
min_sum = INF
answer = 0

for i in range(1, n + 1):
    total = sum(dist[i][1:])
    if total < min_sum:
        min_sum = total
        answer = i

print(answer)
