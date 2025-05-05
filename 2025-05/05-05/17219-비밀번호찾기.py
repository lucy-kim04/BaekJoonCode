import sys
input = sys.stdin.readline

n, m = map(int, input().split())

passwords = dict()

# 저장
for _ in range(n):
    site, pw = input().split()
    passwords[site] = pw

# 조회
for _ in range(m):
    site = input().strip()
    print(passwords[site])
