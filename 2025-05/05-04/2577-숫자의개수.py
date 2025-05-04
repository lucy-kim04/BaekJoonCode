a = int(input())
b = int(input())
c = int(input())

number = a * b * c

for i in range(10):
    print(str(number).count(str(i)))
