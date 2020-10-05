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

def make_comment(num):
    comment = ''
    if 0 <= num < 10:
        # 그냥 다음생을 기대하세요
        comment = '안싸우는게 신기한 사이'
    elif 10 <= num < 20:
        comment = '친해지는것보다 다음생이 더 빠를 사이'
    elif 20 <= num < 30:
        comment = '노오오력 없이 친해지기 힘든 사이'
    elif 30 <= num < 40:
        comment = '전생에 옷깃 한 번 스쳐본 사이'
    elif 40 <= num < 50:
        comment = '얼굴만 알고 지내게 될 사이'
    elif 50 <= num < 60:
        comment = '가끔 안부만 물어 볼 사이'
    elif 60 <= num < 70:
        comment = '언제든 전화 가능한 사이'
    elif 70 <= num < 80:
        comment = '곁에 없으면 허전한 사이'
    elif 80 <= num < 90:
        comment = '눈빛만 봐도 알 수 있을 사이'
    elif 90 <= num < 100:
        comment = '하늘에서 이어준 천생연분~!'
    return comment

def algo(a, b):
    lst_name_num = []
    lst_num = []
    comment = ''

    for n in range(3):
        lst_name_num.append(alpha2num(list(j2hcj(h2j(a[n])))))
        lst_name_num.append(alpha2num(list(j2hcj(h2j(b[n])))))
    lst_num.append(lst_name_num)
    
    while len(lst_name_num) > 2:
        lst_name_num = adda2n(lst_name_num)
        lst_num.append(lst_name_num)

    score = lst_name_num[0]*10 + lst_name_num[1]

    return score, lst_num, make_comment(score)
    # return lst_name_num[0]*10 + lst_name_num[1], lst_num
