expr = input().split('-')

result = 0

for i in range(len(expr)):
    nums = list(map(int, expr[i].split('+')))
    if i == 0:
        result += sum(nums)
    else:
        result -= sum(nums)

print(result)
