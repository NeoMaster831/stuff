l = list(map(int, input().split()))
sum = 0
l.sort()

for i in l:
    sum += i

print(sum // len(l), l[len(l) // 2])