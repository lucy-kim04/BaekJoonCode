N = int(input())

# 1
# 1+6
# 1+6+6*2
# 1+6+6*2+6*3
# 1+6+6*2+6*3+6*4

for i in range(1, N+1):
    if (1+3*(i-1)*i) >=N:
        print(i)
        break