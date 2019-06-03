from konlpy.tag import Okt
from collections import Counter
import os

file_dir = './input'
path_list = [os.path.join(file_dir, file_name) for file_name in os.listdir(file_dir)]

f = open('./stopwords-ko.txt', 'r')

text = []
twitter = Okt()
chat = []
tagged_list = []
wordbox = []
stopword = []

# 해당 단어가 stopword 인지의 여부를 확인해주는 함수
def check_stopword(word):
    if word in stopword:
        return False;
    return True;

# stopword 파일을 읽어 stopword list에 저장
while True:
    line = f.readline().rstrip('\n')
    if not line:
        break
    stopword.append(line)
f.close()

for i in path_list:
    temp = []
    with open(i, 'rt', encoding='UTF8') as f:
        for line in f:
            #print(line)
            line = line.replace("\n", "")
            temp.append(line)
        text.append(temp)

#연령대별 댓글 읽기
for Age_chatlog in text:
    #print(Counter(Age_chatlog))

    #해당 연령대 댓글 하나씩 읽어오기
    for chat in Age_chatlog:
        #print(chat)
        #댓글 형태소 분석
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

print(Counter(wordbox))
