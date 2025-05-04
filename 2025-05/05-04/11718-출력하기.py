while True:
    try:
        line = input()
        print(line)
    except EOFError:
        break

# try -> 오류 날 수도 있는거
# EOF(End of File) -> 파일의 끝
# except -> 오류가 나면 실행
# break -> 반복문 종료
# input() -> 사용자 입력 받기
# print()