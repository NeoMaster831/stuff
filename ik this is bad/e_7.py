def get(u_1):
    if u_1 == 0: # 윷
        print('D', end='')
    elif u_1 == 1: # 걸
        print('C', end='')
    elif u_1 == 2: # 개
        print('B', end='')
    elif u_1 == 3: # 도
        print('A', end='')
    elif u_1 == 4: # 모
        print('E', end='')

u1 = list(map(int, input().split()))
u2 = list(map(int, input().split()))
u3 = list(map(int, input().split()))

u1_1 = 0; u2_1 = 0; u3_1 = 0 # 등

for k in u1:
    if k == 1: u1_1 += 1

for k in u2:
    if k == 1: u2_1 += 1

for k in u3:
    if k == 1: u3_1 += 1

get(u1_1); get(u2_1); get(u3_1)