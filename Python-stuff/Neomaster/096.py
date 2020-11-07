u_txt = 'I love C++, not python'
b_txt = u_txt.encode()
print(u_txt, b_txt)

ret1 = 'I' == u_txt[0]
ret2 = 'I' == b_txt[0]
print(ret1, ret2)