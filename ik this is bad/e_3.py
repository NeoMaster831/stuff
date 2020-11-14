bowls = input()
l_bowls = []
result = 0

for i in bowls:
    l_bowls.append(i)

for it in range(len(l_bowls)):

    if it == 0: # 처음
        result += 10
        continue

    if l_bowls[it - 1] == l_bowls[it]: # 겹쳐있다면
        result += 5
    else: # 아니면
        result += 10

print(result)