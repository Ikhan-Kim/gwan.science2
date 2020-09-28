age = int(input())
# 1살에 18분

time = ((24 / 80) * age)
minute = int(round((time - int(time)) * 60, 1))

if time < 13 :
    print('오전', int(time), '시', minute, '분입니다.')
else:
    print('오후', int(time)-12, '시', minute, '분입니다.')
