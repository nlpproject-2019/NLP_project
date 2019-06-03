from konlpy.tag import Okt
from collections import Counter
import os


#디렉토리는 각자 로컬에 맞춰서 바꿔서 사용!
file_dir = "C:\\Users\\alber\\Desktop\\dev\\NLP_project\\input"
path_list = [os.path.join(file_dir, file_name) for file_name in os.listdir(file_dir)]


text = []
twitter = Okt()
chat = []
tagged_list = []
wordbox = []


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
            #한글자인 단어는 버림
            if len(word) > 1:
                #print(word)
                wordbox.append(word)

print(Counter(wordbox))
