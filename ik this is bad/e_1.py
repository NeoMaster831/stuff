import sys

day = int(input())
car = input().split() # string List
count = 0

if day >= 10:
    print("일의 자리 숫자를 넣으시라고요")
    sys.exit()
if len(car) > 5:
    print("5개 이하로 해달라고요")
    sys.exit()

for iterator in range(len(car)):
    car[iterator] = int(car[iterator])

    # 추가 검사

    if car[iterator] >= 10:
        print("일의 자리 숫자를 넣으라고요")
        sys.exit()

for iterator in range(len(car)):
    if car[iterator] is day:
        count += 1

print(count)