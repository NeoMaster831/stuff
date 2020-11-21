s = input()
cnt = 0
cnt2 = 0

for i in range(len(s)):
    if s[i] == '(':
        cnt += 1
    elif s[i] == ')':
        if s[i-1] == '(':
            cnt -= 1
            cnt2 += cnt
        else:
            cnt -= 1
            cnt2 += 1

print(cnt2)