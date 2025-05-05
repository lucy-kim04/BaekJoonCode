import sys
import heapq
input = sys.stdin.readline

T = int(input())

for _ in range(T):
    k = int(input())
    min_heap = []
    max_heap = []
    visited = [False] * 1_000_001  # 삽입 순서를 인덱스로 추적

    for i in range(k):
        cmd, val = input().split()
        val = int(val)

        if cmd == 'I':
            heapq.heappush(min_heap, (val, i))
            heapq.heappush(max_heap, (-val, i))
            visited[i] = True  # 현재 i번째 값은 유효함

        elif cmd == 'D':
            if val == 1:
                # 최댓값 제거
                while max_heap and not visited[max_heap[0][1]]:
                    heapq.heappop(max_heap)  # 이미 제거된 거면 패스
                if max_heap:
                    visited[max_heap[0][1]] = False
                    heapq.heappop(max_heap)

            elif val == -1:
                # 최솟값 제거
                while min_heap and not visited[min_heap[0][1]]:
                    heapq.heappop(min_heap)
                if min_heap:
                    visited[min_heap[0][1]] = False
                    heapq.heappop(min_heap)

    # 마지막 정리: 유효한 값만 남기기
    while min_heap and not visited[min_heap[0][1]]:
        heapq.heappop(min_heap)
    while max_heap and not visited[max_heap[0][1]]:
        heapq.heappop(max_heap)

    if not min_heap or not max_heap:
        print("EMPTY")
    else:
        print(-max_heap[0][0], min_heap[0][0])
