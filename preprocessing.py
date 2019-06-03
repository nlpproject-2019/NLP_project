from konlpy.tag import Okt
from collections import Counter
import os
import numpy as np

def keyword_extractor(tagger, chatting):
    tokens = tagger.phrases(chatting)
    tokens = [token for token in tokens if len(token) > 1]
    # 한 글자인 단어는 제외
    count_dict = [(token, chatting.count(token)) for token in tokens]
    ranked_words = sorted(count_dict, key=lambda x: x[1], reverse=True)[:10]
    return [keyword for keyword, freq in ranked_words]

file_dir = "C:\\Users\\alber\\Desktop\\dev\\NLP_project\\input"
path_list = [os.path.join(file_dir, file_name) for file_name in os.listdir(file_dir)]


text = []

for i in path_list:
    temp = []
    with open(i, 'rt', encoding='UTF8') as f:
        for line in f:
            #print(line)
            line = line.replace("\n", "")
            temp.append(line)
        text.append(temp)

#print(text[0])
twitter = Okt()
chat = []
tagged_list = []
wordbox = []

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

for i in tagged_list:
    keyword1 = [t[0] for t in i if t[1] == "Noun" or t[1] == "KoreanParticle"]
    if len(keyword1) > 0:
        wordbox.append(keyword1)

result = sum(wordbox, [])
print(Counter(result))