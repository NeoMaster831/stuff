num = input('숫자를 입력하지 않으면 죽임 ㅅㄱ')
try:
    num = int(num)
    print(num)
except:
    try:
        num = float(num)
        print(num)
    except:
        print("씨발련아 숫자를 입력하라고")