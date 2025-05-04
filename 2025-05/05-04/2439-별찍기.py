number = input()
N = int(number)
for i in range(N):
    print(' '*(N-i-1) + '*'*(i+1))