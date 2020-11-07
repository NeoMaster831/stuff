url = 'https://github.com/NeoMaster831/stuff/tree/main/Python-stuff'
log = 'name:홍길동전엌ㅋㅋㅋ age:17 sex:남자 nation:조선'

ret1 = url.split('/')
print(ret1)

ret2 = log.split()
for data in ret2:
    d1, d2 = data.split(':')
    print(d1, d2)