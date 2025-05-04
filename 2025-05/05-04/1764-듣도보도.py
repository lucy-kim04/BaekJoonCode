import sys
input = sys.stdin.readline

N, M = map(int, input().split())

no_heard = set()
for _ in range(N):
    no_heard.add(input().strip())

no_seen = set()
for _ in range(M):
    no_seen.add(input().strip())

# 교집합구하고 정렬
result = sorted(no_heard & no_seen)

print(len(result))
for name in result:
    print(name)
