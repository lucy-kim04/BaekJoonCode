n = int(input())
a = set(map(int, input().split()))

m = int(input())
targets = list(map(int, input().split()))

for t in targets:
    print(1 if t in a else 0)
