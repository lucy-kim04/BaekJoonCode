# 그니까... 재귀를 사용하겠음
# 사분면으로 나눠서 1사분면일 때는 더할게 없구나
# 2사분면일 때는 2**(n-1)*2니까 2**n을 더하고
# 3사분면일 때는 2**n을 2번 더하고
# 4사분면일 때는 2**n을 3번 더하고

# 다시 거기서 현재 n-1이 기본으로 되어있을테니 거기서 또 다시 하는거임

def z(n, r, c):
    if n == 0:
        return 0

    half = 2 ** (n - 1)
    size = half * half

    if r < half and c < half:          # 1사분면
        return z(n - 1, r, c)
    elif r < half and c >= half:       # 2사분면
        return size + z(n - 1, r, c - half)
    elif r >= half and c < half:       # 3사분면
        return size * 2 + z(n - 1, r - half, c)
    else:                              # 4사분면
        return size * 3 + z(n - 1, r - half, c - half)


N, R, C = map(int, input().split())
print(solve(N, R, C))
