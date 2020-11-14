# INPUT
# 1. {시} {분}
# 2. {걸리는 분}

hour, Min = list(map(int, input().split()))
task = int(input())

Min += task # 일단 더함 -> 13 50 + 20 = 13 70
hour += Min // 60
Min %= 60
hour %= 24

print(hour, Min, sep=' ')