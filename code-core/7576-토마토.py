#이거.... 좌표로 봐야할듯 그니까 x+-1 or y+-1인 곳에만 영향을 줄 수 있고
#그 중에서 -1이 있으면 걔는 안바뀌니까 끝남
# 0이 없어질 때까지 반복횟수 카운트트

from collections import deque

M, N = map(int, input().split())
tomato = [list(map(int, input().split())) for _ in range(N)]

queue = deque()
for i in range(N):
    for j in range(M):
        if tomato[i][j] == 1:
            queue.append((i, j))

# 상, 하, 좌, 우
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

while queue:
    x, y = queue.popleft()

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if 0 <= nx < N and 0 <= ny < M and tomato[nx][ny] == 0:
            tomato[nx][ny] = tomato[x][y] + 1
            queue.append((nx, ny))

# 다 돌고 나서 확인
result = 0
for row in tomato:
    for t in row:
        if t == 0:
            print(-1)
            exit()
    result = max(result, max(row))

print(result - 1)  # 처음에 1부터 시작했으니까 하루 빼줌
