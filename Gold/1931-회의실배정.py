# 튜플 써서.... 변경 안되게 하고...
# 일단 끝나는 시간이 빨라야함!!! 그리고 끝나는 시간이 같으면... 


import sys
input = sys.stdin.readline

n = int(input())
meetings = [tuple(map(int, input().split())) for _ in range(n)]


meetings.sort(key=lambda x: (x[1], x[0])) # 튜플을 역순으로 해서 끝나는 시간이 오름차순으로 정리됨

end_time = 0
count = 0

for start, end in meetings:
    if start >= end_time:
        end_time = end
        count += 1

print(count)

# end_time..... 오늘의 시작이 0이니까 끝나는 시간 오름차순으로 정리했을 때 니 시작시간이 오늘의 시작시간보다 크면 들어와! 근데 니 끝나는 시간을 기준으로 다시 잡아야하니까 end_time에 넣을게 그리고 너 들어갔으니 count 올릴게 
# -> 다음 end_time보다 니가 시작시간이 작네? 니 패스 니가 시작시간이 크네? 너 들어가 자 니 끝나는 시간 다시 기준 잡을게 -> 카운트 올릴게