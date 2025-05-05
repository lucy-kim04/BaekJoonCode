from collections import deque

N, K = map(int, input().split())

MAX = 100001
visited = [0] * MAX

def bfs(start):
    queue = deque([start])
    while queue:
        now = queue.popleft()
        if now == K:
            return visited[now]
        
        for next_pos in [now - 1, now + 1, now * 2]:
            if 0 <= next_pos < MAX and visited[next_pos] == 0:
                visited[next_pos] = visited[now] + 1
                queue.append(next_pos)

print(bfs(N))
