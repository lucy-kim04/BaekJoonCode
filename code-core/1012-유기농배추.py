import sys
sys.setrecursionlimit(10000)  # 재귀 깊이 늘려줌
input = sys.stdin.readline

T = int(input())  # 테스트 케이스 수

for _ in range(T): # 배추 K개 심고 for문 끝났으니 그 다음꺼부터 다시 시작 -> T번 반복해라!
    M, N, K = map(int, input().split())  # 가로, 세로, 배추 개수

    graph = [[0] * M for _ in range(N)]  # 배추 밭 0으로 표현하기!

    visited = [[False] * M for _ in range(N)]  # 방문 확인용

    for _ in range(K):
        x, y = map(int, input().split())
        graph[y][x] = 1  # 배추 심기(이거 [x][y]랑 안 헷갈리게 조심!)

    # DFS 함수
    def dfs(x, y):
        visited[y][x] = True

        for dx, dy in [(-1,0),(1,0),(0,-1),(0,1)]:
            nx = x + dx
            ny = y + dy
            if 0 <= nx < M and 0 <= ny < N: # 배추밭 안에 있는가
                if not visited[ny][nx] and graph[ny][nx] == 1: # 안가봤고, 배추가 있는가
                    dfs(nx, ny) # 그러면 다시 이 함수 실행시켜서 또 움직여라!

    count = 0
    for y in range(N):
        for x in range(M):
            if graph[y][x] == 1 and not visited[y][x]:
                dfs(x, y)
                count += 1 # 지렁이 필요한 곳에 넣기 -> dfs 실행

    print(count)
