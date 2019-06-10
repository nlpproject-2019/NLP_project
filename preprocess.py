<<<<<<< HEAD
from konlpy.tag import Okt
from collections import Counter
import os


file_dir = './input'
path_list = [os.path.join(file_dir, file_name) for file_name in os.listdir(file_dir)]

text = []
twitter = Okt()
chat = []
tagged_list = []
wordbox = []
stopword = []

# 해당 단어가 stopword 인지의 여부를 확인해주는 함수
def check_stopword(word):

    f = open('./stopwords-ko.txt', 'r')
    while True:
        line = f.readline().rstrip('\n')
        if not line:
            break
        stopword.append(line)
    f.close()

    if word in stopword:
        return False;
    return True;

# stopword 파일을 읽어 stopword list에 저장

def PreprocessComment(Comment):
    Comment_word = []
    tokens = twitter.pos(Comment, norm=True, stem=False)

    # Noun 과 KoreanParticle 만 골라서 담기
    for i in tokens:
        if i[1] == "Noun" or i[1] == "KoreanParticle":
            Comment_word.append(i[0])
    return Counter(Comment_word)

print(PreprocessComment("안녕하세요 반갑습니다 이름이 뭐에요? ㅋㅋㅋ 이름"))



def PreprocessFiles(file_dir):

    path_list = [os.path.join(file_dir, file_name) for file_name in os.listdir(file_dir)]
    for i in path_list:
        temp = []
        with open(i, 'rt', encoding='UTF8') as f:
            for line in f:
                # print(line)
                line = line.replace("\n", "")
                temp.append(line)
            text.append(temp)

    # 연령대별 댓글 읽기
    for Age_chatlog in text:
        # print(Counter(Age_chatlog))

        # 해당 연령대 댓글 하나씩 읽어오기
        for chat in Age_chatlog:
            # print(chat)
            # 댓글 형태소 분석
            k = twitter.pos(chat, norm=True, stem=False)
            tagged_list.append(k)
        break

    # Noun 과 KoreanParticle 만 골라서 담기
    for i in tagged_list:
        Noun_KoreanParticle = [t[0] for t in i if t[1] == "Noun" or t[1] == "KoreanParticle"]

        if len(Noun_KoreanParticle) > 0:
            for word in Noun_KoreanParticle:
                if check_stopword(word):
                    wordbox.append(word)

    x = Counter(wordbox)
    #print(x)
    #print(len(x.keys()))

    return x
=======
import math
import time
import numpy as np

from collections import Counter
from konlpy.tag import Okt 
okt=Okt()

# (전처리) 길이가 2이상인 명사만 고르기
def get_nouns(text):
    nouns = okt.nouns(text)
    nouns = [word for word in nouns if len(word) > 1]
    return nouns

wordbox = []

file = open("input/10.txt", 'r', encoding='UTF8')
doc = file.read()
file.close()
token = get_nouns(doc)
wordbox.append(Counter(token))

file = open("input/20.txt", 'r', encoding='UTF8')
doc = file.read()
file.close()
token = get_nouns(doc)
wordbox.append(Counter(token))

file = open("input/30.txt", 'r', encoding='UTF8')
doc = file.read()
file.close()
token = get_nouns(doc)
wordbox.append(Counter(token))

file = open("input/40.txt", 'r', encoding='UTF8')
doc = file.read()
file.close()
token = get_nouns(doc)
wordbox.append(Counter(token))

file = open("input/50.txt", 'r', encoding='UTF8')
doc = file.read()
file.close()
token = get_nouns(doc)
wordbox.append(Counter(token))
>>>>>>> weighting
