from collections import deque # double ended queue

N, M, V = map(int, input().split())
graph = [[] for _ in range(N+1)]

# 양방향!!!! 그래프 만들기
for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

# 작은 번호 먼저 방문하도록 정렬
for g in graph:
    g.sort()

# DFS
def dfs(node, visited):
    visited[node] = True
    print(node, end=' ')
    for neighbor in graph[node]:
        if not visited[neighbor]:
            dfs(neighbor, visited)

# BFS
def bfs(start):
    visited = [False] * (N + 1)
    queue = deque([start])
    visited[start] = True

    while queue:
        node = queue.popleft()
        print(node, end=' ')
        for neighbor in graph[node]:
            if not visited[neighbor]:
                visited[neighbor] = True
                queue.append(neighbor)

# 실행
visited_dfs = [False] * (N + 1)
dfs(V, visited_dfs)
print()
bfs(V)

# DFS
# 깊이 우선 탐색, Depth-First-Search
# 가장 깊은 노드까지 먼저 탐색 -> 막히면 -> 돌아와서 다른 갈래 탐색
# 스택 or 재귀 함수 활용

# BFS
# 너비 우선 탐색, Breadth-First-Search
# 가장 가까운 노드부터 탐색 -> 여러 갈래 탐색 가능
# 큐 or 반복문 활용