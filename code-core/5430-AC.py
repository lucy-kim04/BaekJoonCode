from collections import deque
import sys
input = sys.stdin.readline

T = int(input())

for _ in range(T): # 케이스가 T니까 반복해라
    p = input().strip() # 함수 이름
    n = int(input()) # 배열 크기
    arr = input().strip() # 배열열

    if n == 0:
        dq = deque() # 빈 배열일 때 아래꺼 쓰면 오류 나니까 빈 deque 만들기
    else:
        dq = deque(map(int, arr[1:-1].split(',')))  # [1,2,3] → 1 2 3, arr[1:-1] -> 두번째 문자([ 이거 빼고)부터 마지막까지

    reverse = False
    error = False

    for cmd in p:
        if cmd == 'R':
            reverse = not reverse
        elif cmd == 'D':
            if not dq:
                error = True
                break
            if reverse:
                dq.pop()
            else:
                dq.popleft()

    if error:
        print("error")
    else:
        if reverse:
            dq.reverse()
        print("[" + ",".join(map(str, dq)) + "]")
