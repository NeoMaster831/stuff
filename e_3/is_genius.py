w, h = map(int, input().split())
p, q = map(int, input().split())
t = int(input())

psw = 1
qsw = 1

for i in range(t % (w*2)):
    p += psw
    if p >= w or p <= 0:
        psw *= -1 

for i in range(t % (h*2)):
    q += qsw
    if q >= h or q <= 0:
        qsw *= -1

print(p,q)
