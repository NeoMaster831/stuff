l_pass = list(map(int, input().split()))
g = 0

for s in range(len(l_pass)):
    o = int(l_pass[s])
    g += o ** 2

g %= 10

print(g)