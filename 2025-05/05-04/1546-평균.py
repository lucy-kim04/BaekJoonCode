n = int(input())
scores = list(map(int, input().split()))
topscore = max(scores)

total = 0
for score in scores:
    total += (score / topscore) * 100

avg = total / n
print(avg)
