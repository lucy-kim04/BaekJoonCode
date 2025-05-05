from collections import deque
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]
dist = [[-1] * m for _ in range(n)]

# 출발점 찾기
for i in range(n):
    for j in range(m):
        if board[i][j] == 2:
            start = (i, j)
            dist[i][j] = 0  # 자기 자신은 거리 0

# BFS
queue = deque([start])
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

while queue:
    x, y = queue.popleft()
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < n and 0 <= ny < m:
            if board[nx][ny] == 1 and dist[nx][ny] == -1:
                dist[nx][ny] = dist[x][y] + 1
                queue.append((nx, ny))

# 갈 수 없는 곳이 0이면 0으로, 1인데 못 갔으면 -1
for i in range(n):
    for j in range(m):
        if board[i][j] == 0:
            print(0, end=' ')
        else:
            print(dist[i][j], end=' ')
    print()
