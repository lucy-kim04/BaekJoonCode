import sys
input = sys.stdin.readline

M = int(input())
S = 0  # 비어있는 집합 (비트마스크)

for _ in range(M):
    cmd = input().strip().split()

    if cmd[0] == 'add':
        x = int(cmd[1])
        S |= (1 << (x - 1))
    elif cmd[0] == 'remove':
        x = int(cmd[1])
        S &= ~(1 << (x - 1))
    elif cmd[0] == 'check':
        x = int(cmd[1])
        print(1 if S & (1 << (x - 1)) else 0)
    elif cmd[0] == 'toggle':
        x = int(cmd[1])
        S ^= (1 << (x - 1))
    elif cmd[0] == 'all':
        S = (1 << 20) - 1
    elif cmd[0] == 'empty':
        S = 0
