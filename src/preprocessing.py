#-*- coding:utf-8 -*-

from konlpy.tag import Okt
from collections import Counter
import os

text = []
twitter = Okt()
chat = []
wordbox = []
stopword = []

# stopword 파일을 읽어 stopword list에 저장
f = open('./stopwords-ko.txt', 'rt', encoding='UTF8')

while True:
    line = f.readline().rstrip('\n')
    if not line:
        break
    stopword.append(line)
f.close()

#댓글의 형태소 분석
def PreprocessComment(Comment):
    Comment_word = []
    tokens = twitter.pos(Comment, norm=True, stem=False)

    # Noun 과 KoreanParticle 만 골라서 담기
    for i in tokens:
        if i[1] == "Noun" or i[1] == "KoreanParticle":
            if i[1] not in stopword:
                Comment_word.append(i[0])
    return Counter(Comment_word)


#DataSet 의 전처리 과정
def PreprocessFiles(file_dir):
    All_tagged_list = []
    path_list = [os.path.join(file_dir, file_name) for file_name in os.listdir(file_dir)]
    for i in path_list:
        temp = []
        with open(i, 'rt', encoding='UTF8') as file:
            for line in file:
                line = line.replace("\n", "")
                tagged_list = twitter.pos(line, norm=True, stem=False)
                for j in tagged_list:
                    #stopwords 거나 noun, koreanparticle 이 아니라면 제외!
                    if j[1] == "Noun" or j[1] == "KoreanParticle":
                        if j[0] not in stopword:
                            #print(j[0])
                            temp.append(j[0])
        All_tagged_list.append(Counter(temp))
                               
    return All_tagged_list
