d1, e1 = list(map(int, input().split()))
d2, e2 = list(map(int, input().split()))
d3, e3 = list(map(int, input().split()))
d4, e4 = list(map(int, input().split()))
now = 0
highpoint = now

# d{x} 는 내린사람, e{x] 는 탄사람
# result - d{x} 를 먼저 한 후 + e{x} 를 함

now -= d1; now += e1
if highpoint < now:
    highpoint = now

now -= d2; now += e2
if highpoint < now:
    highpoint = now

now -= d3; now += e3
if highpoint < now:
    highpoint = now

now -= d4; now += e4
if highpoint < now:
    highpoint = now

print(highpoint)