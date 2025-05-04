n = int(input())

factorial = 1
for i in range(1, n + 1):
    factorial *= i

# 팩토리얼 결과를 문자열로 변환
factorial_str = str(factorial)

# 뒤에서부터 0 세기
count = 0
for char in reversed(factorial_str):
    if char == '0':
        count += 1
    else:
        break

print(count)
