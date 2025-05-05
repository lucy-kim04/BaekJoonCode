n = int(input())
nums = list(map(int, input().split()))

# 1. 중복 제거 + 정렬
sorted_unique = sorted(set(nums))

# 2. 좌표 압축 매핑
coord_map = {num: idx for idx, num in enumerate(sorted_unique)}

# 3. 압축 결과 출력
print(' '.join(str(coord_map[num]) for num in nums))
