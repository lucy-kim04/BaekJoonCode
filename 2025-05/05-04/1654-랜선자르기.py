import sys

K, N = map(int, input().split())
lines = [int(sys.stdin.readline()) for _ in range(K)]

start = 1
end = max(lines)
result = 0

while start <= end:
    mid = (start + end) // 2
    count = sum(line // mid for line in lines)

    if count >= N:
        result = mid  # 일단 저장하고 더 크게 자를 수 있는지 탐색
        start = mid + 1
    else:
        end = mid - 1

print(result)
