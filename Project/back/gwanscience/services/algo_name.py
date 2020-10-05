from jamo import h2j, j2hcj, j2h

vo2num = {'ㄱ': 2, 'ㄴ': 2, 'ㄷ': 3, 'ㄹ': 5, 'ㅁ': 4, 'ㅂ': 4, 'ㅅ': 2, 'ㅇ': 1, 'ㅈ': 3, 'ㅊ': 4, 'ㅋ': 3, 'ㅌ': 4, 'ㅍ': 4, 'ㅎ': 3,
    'ㄲ': 4, 'ㄸ': 6, 'ㅃ': 8, 'ㅆ': 4, 'ㅉ': 6, 'ㅏ': 2, 'ㅑ': 3, 'ㅓ': 2, 'ㅕ': 3, 'ㅗ': 2, 'ㅛ': 3, 'ㅜ': 2, 'ㅠ': 3, 'ㅡ': 1, 'ㅣ': 1,
    'ㅐ': 3, 'ㅒ': 4, 'ㅔ': 3, 'ㅖ': 4, 'ㅘ': 4, 'ㅙ': 5, 'ㅚ': 3, 'ㅝ': 4, 'ㅞ': 5, 'ㅟ': 3, 'ㅢ': 2,
    'ㄳ': 4, 'ㄵ': 5, 'ㄶ': 5, 'ㄺ': 7, 'ㄻ': 9, 'ㄼ': 9, 'ㄽ': 7, 'ㄾ': 9, 'ㄿ': 9, 'ㅀ': 8, 'ㅄ': 6,
    }

# 각 자모를 획수로 반환
def alpha2num(alpha):
    result = 0
    for a in alpha:
        result += vo2num[a]
    return result

# 옆의 획수를 더해 값 출력
def adda2n(lst_num):
    lst_result = []
    for n in range(len(lst_num)-1):
        result = lst_num[n] + lst_num[n+1]
        lst_result.append(result%10)
    return lst_result

def algo(a, b):
    lst_name_num = []
    lst_num = []

    for n in range(3):
        lst_name_num.append(alpha2num(list(j2hcj(h2j(a[n])))))
        lst_name_num.append(alpha2num(list(j2hcj(h2j(b[n])))))
    lst_num.append(lst_name_num)
    
    while len(lst_name_num) > 2:
        lst_name_num = adda2n(lst_name_num)
        lst_num.append(lst_name_num)

    if lst_name_num == [0, 0]:
        return 100, lst_num
    else:
        return lst_name_num[0]*10 + lst_name_num[1], lst_num
