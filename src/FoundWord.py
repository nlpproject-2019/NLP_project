#'초성'은 음절의 구성에서 처음 소리인 자음이고, '중성'은 음절의 구성에서 중간 소리인 모음 '종성'은 음절의 구성에서 마지막 소리인 자음 예를 들어, '감'에서 'ㄱ'은 초성, 'ㅏ'는 중성, 'ㅁ'은 종성


# 초성 리스트. 00 ~ 18
CHOSUNG_LIST = ['ㄱ', 'ㄲ', 'ㄴ', 'ㄷ', 'ㄸ', 'ㄹ', 'ㅁ', 'ㅂ', 'ㅃ', 'ㅅ', 'ㅆ', 'ㅇ', 'ㅈ', 'ㅉ', 'ㅊ', 'ㅋ', 'ㅌ', 'ㅍ', 'ㅎ']
# 중성 리스트. 00 ~ 20
JUNGSUNG_LIST = ['ㅏ', 'ㅐ', 'ㅑ', 'ㅒ', 'ㅓ', 'ㅔ', 'ㅕ', 'ㅖ', 'ㅗ', 'ㅘ', 'ㅙ', 'ㅚ', 'ㅛ', 'ㅜ', 'ㅝ', 'ㅞ', 'ㅟ', 'ㅠ', 'ㅡ', 'ㅢ',
                 'ㅣ']
# 종성 리스트. 00 ~ 27 + 1(1개 없음)
JONGSUNG_LIST = [' ', 'ㄱ', 'ㄲ', 'ㄳ', 'ㄴ', 'ㄵ', 'ㄶ', 'ㄷ', 'ㄹ', 'ㄺ', 'ㄻ', 'ㄼ', 'ㄽ', 'ㄾ', 'ㄿ', 'ㅀ', 'ㅁ', 'ㅂ', 'ㅄ', 'ㅅ',
                 'ㅆ', 'ㅇ', 'ㅈ', 'ㅊ', 'ㅋ', 'ㅌ', 'ㅍ', 'ㅎ']

data_example = ['빨', '노', '초', '파', '막', '식으루', '쨍', '색도', '관심', '법']

def word_decomposition(korean_word):
    r_lst = []
    for w in list(korean_word.strip()):
        ## 영어인 경우 구분해서 작성함.
        if '가' <= w <= '힣':
            ## 588개 마다 초성이 바뀜.
            ch1 = (ord(w) - ord('가')) // 588
            ## 중성은 총 28가지 종류
            ch2 = ((ord(w) - ord('가')) - (588 * ch1)) // 28
            ch3 = (ord(w) - ord('가')) - (588 * ch1) - 28 * ch2
            r_lst.append([CHOSUNG_LIST[ch1], JUNGSUNG_LIST[ch2], JONGSUNG_LIST[ch3]])
        else:
            r_lst.append([w])
    r_lst = sum(r_lst, [])
    return r_lst

def find_word_in_List(new_word, data_list):
    part_of_new_word = word_decomposition(new_word)
    before_distance = 0
    
    for keyword in data_list:
        distance = 0
        if len(new_word) - len(keyword) != 0 or len(keyword) == 1:
            continue
        part_of_keyword =word_decomposition(keyword)
        
        #새로운 단어의 모음 자음이 데이터셋에 있는 단어와 최대한 같은 단어를 찾아감
        for i, j in enumerate(part_of_new_word):
            if part_of_keyword[i] == j:
                distance += 1
                continue
            else:
                break

#print(distance)
#print(keyword)
#print("++++")

if distance > before_distance:
    return_word = keyword
        before_distance = distance
    
    if before_distance == 0:
        print("알맞는 단어가 존재하지 않습니다.")
else:
    return return_word




#print(find_word_in_List("안녕하세요", ["안녕", "하세요", "만나서", "반갑습니다", "뭐하고", "뭐라고했냐?", "뭐라고씨불?", "뭐라고씨발!"]))


#print(word_decomposition("ㅋㅋㅋㅋ"))
