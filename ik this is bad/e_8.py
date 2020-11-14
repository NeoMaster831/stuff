d, s = list(map(int, input().split()))
o = []
# d는 수, s는 K

for i in range(1, d):
    if d % i == 0:
        o.append(i)

# if d = 6, o = [ 1, 2, 3, 6 ]
# 어짜피 오름차순으로 정렬됨.
try:
    print(o[s - 1])
except IndexError:
    print(0)