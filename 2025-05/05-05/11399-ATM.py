n = int(input())
times = list(map(int, input().split()))

times.sort()  # 적은 시간부터 정렬

total = 0
acc = 0

for t in times:
    acc += t       # 지금까지 누적 시간
    total += acc   # 누적 시간의 합을 더함

print(total)
