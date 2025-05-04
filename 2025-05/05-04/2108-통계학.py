import sys
from collections import Counter

n = int(sys.stdin.readline())
nums = [int(sys.stdin.readline()) for _ in range(n)]

nums.sort()

# 산술평균균
print(round(sum(nums) / n))

# 중앙값...
print(nums[n // 2])

# 최빈값
count = Counter(nums)
most = count.most_common()
max_freq = most[0][1]
modes = [num for num, freq in most if freq == max_freq]

if len(modes) > 1:
    print(sorted(modes)[1]) 
else:
    print(modes[0])

# 범위!
print(nums[-1] - nums[0])
