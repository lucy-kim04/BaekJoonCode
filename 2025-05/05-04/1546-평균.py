n = int(input())
scores = list(map(int, input().split()))
total = sum(scores)
avg = total / n
print(avg)
