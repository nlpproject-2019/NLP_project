import math
import time
import numpy as np

start_time = time.time()

from konlpy.tag import Okt 
okt=Okt()

#
def get_nouns(text):
    nouns = okt.nouns(text)
    nouns = [word for word in nouns if len(word) > 1]
    return nouns

doc_name = ['10', '20', '30', '40', '50']
doc_token = []

#
for name in doc_name:
    file = open("data/"+ name +".txt", 'r', encoding='UTF8')
    doc = file.read()
    file.close()

    token = get_nouns(doc)
    doc_token.append(token)

#
word2index = {}
for token in doc_token:
    for voca in token:
        if voca not in word2index.keys():
            word2index[voca] = len(word2index)

#
TF = []
for token in doc_token:
    freq = []
    for word in word2index.keys():
        freq.append(token.count(word))
    freq_max = max(freq)
    for i in range(0, len(freq)):
        freq[i] = freq[i] / freq_max
    TF.append(freq)

#
IDF = []
for i in range(0, len(TF[0])):
    num = 0
    for tf in TF:
        if tf[i] != 0:
            num+=1
    idf = math.log10(len(doc_name) / num)
    IDF.append(idf)

#
WEIGHT = []
for tf in TF:
    weight = []
    for i in range(0, len(tf)):
        weight.append(tf[i] * IDF[i])
    WEIGHT.append(weight)

    rankIdx = list(np.argsort(np.array(weight)))
    rankIdx.reverse()

    for idx in range(0,5):
        for key, value in word2index.items():
            if value == rankIdx[idx]:
                print(key)
    print("")

end_time = time.time()
print("WorkingTime: {} sec".format(end_time-start_time))