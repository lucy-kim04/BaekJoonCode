P = int(input())

for _ in range(P):
  data = list(map(int, input().split()))
  T = data[0]

  count = 0
  line = []

  for x in x: # 키 고르기
    for i in range(len(line)): # 키 비교
      if line[i] > x:
        count += 1
  