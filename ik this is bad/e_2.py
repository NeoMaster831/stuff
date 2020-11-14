import sys

input_ = list(map(int, input().split()))

if len(input_) > 3:
    print("3번만...")
    sys.exit()

price = input_[0]
count = input_[1]
money = input_[2]

if price * count - money < 0:
    print(0)
else: print(price * count - money)