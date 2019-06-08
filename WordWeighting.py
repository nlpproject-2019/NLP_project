import math
'''
# Indexing
input: wordbox(전처리하고 문서별로 토큰화된것, 형식: Counter)
output: word2index(인덱싱한것, 형식: Dictionary(단어:index넘버))
'''
def Indexing(wordbox): 
    word2index = {}
    for token in wordbox:
        for voca in token:
            if voca not in word2index.keys():
                word2index[voca] = len(word2index)
    return word2index
'''
# TF
input: word2index(인덱싱한것, 형식: Dictionary(단어:index넘버)), wordbox(전처리하고 문서별로 토큰화된것, 형식: Counter)
output: TF(TF, 형식: list([[],[],[],[],[]])
'''
def TF(word2index, wordbox):
    TF = []
    for token in wordbox:
        tf = []
        for voca in word2index.keys():
            if voca not in token:
                tf.append(0)
            else:
                tf.append(token[voca])
        tf_max = max(tf)
        for i in range(0, len(tf)):
            tf[i] = tf[i] / tf_max
        TF.append(tf)
    return TF
'''
# IDF
input: TF(TF, 형식: list([[],[],[],[],[]])
output: IDF(TF, 형식: list([])
'''
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
'''
# Weighting
input: TF(TF, 형식: list([[],[],[],[],[]]), IDF(TF, 형식: list([])
output: Weight(Weight=TF*IDF, 형식: list([[],[],[],[],[]])
'''
def Weighting(TF, IDF):
    Weight = []
    for tf in TF:
        weight = []
        for i in range(0, len(tf)):
            weight.append(tf[i] * IDF[i])
        Weight.append(weight)
    return Weight