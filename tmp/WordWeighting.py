
##----------------------------------------------
## 실험용 # wordbox 넘겨받음
#from collections import Counter
#doc1 = ['가', '나', '다', '라']
#doc2 = ['가', '나']
#doc3 = ['마', '마', '바', '사']
#doc4 = ['카', '타']
#doc5 = ['바']

#wordbox = []
#wordbox.append(Counter(doc1))
#wordbox.append(Counter(doc2))
#wordbox.append(Counter(doc3))
#wordbox.append(Counter(doc4))
#wordbox.append(Counter(doc5))
##----------------------------------------------

from collections import Counter
import math
from preprocessing import wordbox # wordbox

def Indexing(wordbox): 
    word2index = {}
    for token in wordbox:
        for voca in token:
            if voca not in word2index.keys():
                word2index[voca] = len(word2index)
    return word2index

def TF(list_Indexing, wordbox):
    TF = []
    for token in wordbox:
        tf = []
        for voca in list_Indexing.keys():
            if voca not in token:
                tf.append(0)
            else:
                tf.append(token[voca])
        tf_max = max(tf)
        for i in range(0, len(tf)):
            tf[i] = tf[i] / tf_max
        TF.append(tf)
    return TF

def IDF(TF):
    IDF = []
    for i in range(0, len(TF[0])):
        num = 0
        for tf in TF:
            if tf[i] != 0:
                num+=1
        idf = math.log10(len(TF) / num)
        IDF.append(idf)
    return IDF

def Weighting(TF, IDF):
    Weight = []
    for tf in TF:
        weight = []
        for i in range(0, len(tf)):
            weight.append(tf[i] * IDF[i])
        Weight.append(weight)
    return Weight

list_Indexing = Indexing(wordbox)
word_TF = TF(list_Indexing, wordbox)
word_IDF = IDF(word_TF)
word_Weight = Weighting(word_TF, word_IDF)