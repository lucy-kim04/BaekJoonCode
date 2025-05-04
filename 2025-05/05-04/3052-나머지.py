nums = [int(input()) for _ in range(10)]
remainders = set()

for num in nums:
    remainders.add(num % 42)

print(len(remainders))
