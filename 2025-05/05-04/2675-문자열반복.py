t = int(input())

for _ in range(t):
    r, s = input().split()
    r = int(r)
    for char in s:
        print(char * r, end='')
    print()
