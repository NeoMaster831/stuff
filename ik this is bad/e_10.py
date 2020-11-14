l1 = list(map(int, input().split()))
l2 = []
sum = 0

for i in l1:
    if i % 2 == 1:
        l2.append(i)

for i in l2:
    sum += i

print(sum, min(l2), sep=' ')