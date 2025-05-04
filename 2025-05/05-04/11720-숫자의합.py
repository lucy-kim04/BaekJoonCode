N = int(input())           # 숫자 개수 (실제로 안 써도 되지만 형식상 받기)
digits = input()           # 문자열 그대로 받기
total = sum(map(int, digits))  # 문자열 각각을 int로 바꿔서 더함
print(total)
