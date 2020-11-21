size = list(map(int, input().split())) # size = [ x, y ]
tmpx, tmpy = list(map(int, input().split()))
fort = int(input())

mode = 1

# mode 1 = (+, +)  ↗
# mode 2 = (-, +)  ↖
# mode 3 = (+, -)  ↘
# mode 4 = (-, -)  ↙

for i in range(fort):
    tmpx_ = tmpx; tmpy_ = tmpy
    if mode == 1:
        tmpx_ += 1;  tmpy_ += 1

        # case 1: tmpx > size[0]
        if tmpx_ > size[0]:
            mode = 2
            tmpx -= 1; tmpy += 1

        # case 2: tmpy > size[0]
        if tmpy > size[1]:
            mode = 3
            tmpx += 1; tmpy -= 1
    
    elif mode == 2:
        tmpx_ -= 1; tmpy_ += 1

        # case 1: tmpx < 0
        if tmpx_ < 0:
            mode = 1
            tmpx += 1; tmpy += 1
        
        # case 2: tmpy > size[1]
        if tmpy_ > size[1]:
            mode = 4
            tmpx -= 1; tmpy -= 1
    
    elif mode == 3:
        tmpx_ += 1; tmpy_ -= 1

        # case 1: tmpx > size[0]
        if tmpx_ > size[0]:
            mode = 4
            tmpx -= 1; tmpy -= 1
        
        # case 2: tmpy < 0
        if tmpy_ < 0:
            mode = 1
            tmpx += 1; tmpy += 1
    
    else:
        tmpx_ -= 1; tmpy_ -= 1

        # case 1: tmpx < 0
        if tmpx_ < 0:
            mode = 3
            tmpx += 1; tmpy -= 1
        
        #case 2: tmpy < 0
        if tmpy_ < 0:
            mode = 2
            tmpx -= 1; tmpy += 1

print(tmpx, tmpy)