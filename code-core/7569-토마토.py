from collections import deque
import sys
input = sys.stdin.readline

M, N, H = map(int, input().split())  # 가로, 세로, 높이

# 3차원 배열 만들기
box = [[[0] * M for _ in range(N)] for _ in range(H)]

queue = deque()

# 입력 받기 & 익은 토마토 큐에 넣기
for h in range(H):
    for n in range(N):
        row = list(map(int, input().split()))
        for m in range(M):
            box[h][n][m] = row[m]
            if row[m] == 1:
                queue.append((h, n, m))  # (z, x, y)

# 6방향 이동
dz = [0, 0, 0, 0, 1, -1]
dx = [-1, 1, 0, 0, 0, 0]
dy = [0, 0, -1, 1, 0, 0]

while queue:
    z, x, y = queue.popleft()
    for i in range(6):
        nz, nx, ny = z + dz[i], x + dx[i], y + dy[i]
        if 0 <= nz < H and 0 <= nx < N and 0 <= ny < M:
            if box[nz][nx][ny] == 0:
                box[nz][nx][ny] = box[z][x][y] + 1
                queue.append((nz, nx, ny))

# 결과 확인
res = 0
for h in range(H):
    for n in range(N):
        for m in range(M):
            if box[h][n][m] == 0:
                print(-1)
                sys.exit(0)
            res = max(res, box[h][n][m])

print(res - 1)  # 시작이 1이니까 -1 해줌
