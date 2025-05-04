n = int(input())

for _ in range(n):
    quiz = input()
    score = 0
    count = 0

    for ch in quiz:
        if ch == 'O':
            count += 1
            score += count
        else:
            count = 0

    print(score)
