n = int(input())
paper = [list(map(int, input().split())) for _ in range(n)]

white = 0
blue = 0

def check(x, y, size):
    global white, blue
    color = paper[x][y]
    for i in range(x, x + size):
        for j in range(y, y + size):
            if paper[i][j] != color:
                half = size // 2
                check(x, y, half)                # 왼쪽 위
                check(x, y + half, half)         # 오른쪽 위
                check(x + half, y, half)         # 왼쪽 아래
                check(x + half, y + half, half)  # 오른쪽 아래
                return
    
    # 전부 같은 색이면
    if color == 0:
        white += 1
    else:
        blue += 1

check(0, 0, n)
print(white)
print(blue)
