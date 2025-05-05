n, m = map(int, input().split())
trees = list(map(int, input().split()))

low = 0
high = max(trees)
result = 0

while low <= high:
    mid = (low + high) // 2
    total = sum((tree - mid) for tree in trees if tree > mid)

    if total >= m:
        result = mid  # 조건 만족했으니 일단 저장
        low = mid + 1  # 더 높은 높이도 시도
    else:
        high = mid - 1  # 너무 조금 잘랐으니 낮춰야 함

print(result)
