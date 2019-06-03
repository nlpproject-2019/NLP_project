from konlpy.tag import Okt

import os

file_dir = "C:\\Users\\alber\\Desktop\\dev\\NLP_project\\input"
path_list = [os.path.join(file_dir, file_name) for file_name in os.listdir(file_dir)]


text = []

for i in path_list:
    temp = []
    with open(i, 'rt', encoding='UTF8') as f:
        for line in f:
            #print(line)
            temp.append(line)
        text.append(temp)

print(text[0])
twitter = Okt()
chat = []
for chatlog in text:
    for chat in chatlog:
        k = twitter.pos(chat, norm=True, stem=False)
        print(k)
    break

