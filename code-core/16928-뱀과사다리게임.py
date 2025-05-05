from collections import deque

N, M = map(int, input().split())

move = {}  # 사다리/뱀 이동 정보 저장

# 사다리
for _ in range(N):
    a, b = map(int, input().split())
    move[a] = b

# 뱀
for _ in range(M):
    a, b = map(int, input().split())
    move[a] = b

visited = [False] * 101 # 0번은 안쓰니까 101 해줘야함!!

def bfs():
    queue = deque()
    queue.append((1, 0))  # (현재 위치, 주사위 횟수)
    visited[1] = True # 중복 방문 막기 -> 지금 최소 찾고 있으니까...

    while queue: # 계속 반복해라
        pos, count = queue.popleft()

        if pos == 100:
            return count

        for dice in range(1, 7):  # range는 마지막 숫자 포함 안되기 때문에 7로 표시!
            next_pos = pos + dice
            if next_pos > 100:
                continue # 100번 칸에 정확히! 도착! 해야하기 때문에 다음꺼 던지기기

            # 사다리/뱀 타기
            if next_pos in move:
                next_pos = move[next_pos]

            if not visited[next_pos]:
                visited[next_pos] = True
                queue.append((next_pos, count + 1))

print(bfs())


# 첫째 줄에 게임판에 있는 사다리의 수 N(1 ≤ N ≤ 15)과 뱀의 수 M(1 ≤ M ≤ 15)이 주어진다.

# 둘째 줄부터 N개의 줄에는 사다리의 정보를 의미하는 x, y (x < y)가 주어진다. x번 칸에 도착하면, y번 칸으로 이동한다는 의미이다.

# 다음 M개의 줄에는 뱀의 정보를 의미하는 u, v (u > v)가 주어진다. u번 칸에 도착하면, v번 칸으로 이동한다는 의미이다.

# 1번 칸과 100번 칸은 뱀과 사다리의 시작 또는 끝이 아니다. 모든 칸은 최대 하나의 사다리 또는 뱀을 가지고 있으며, 동시에 두 가지를 모두 가지고 있는 경우는 없다. 항상 100번 칸에 도착할 수 있는 입력만 주어진다.