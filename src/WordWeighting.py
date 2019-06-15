#-*- coding:utf-8 -*-
from FoundWord import *
import math
import numpy as np

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
def TF(word2index, wordbox, bool):
    if bool == 'word':
        TF = []
        for token in wordbox:
            tf = []
            for voca in word2index.keys():
                if voca not in token.keys():
                    tf.append(0)
                else:
                    tf.append(token[voca])
            tf_max = max(tf)
            for i in range(0, len(tf)):
                tf[i] = tf[i] / tf_max
            TF.append(tf)

    elif bool == 'query':
        TF = []
        for token in wordbox:
            tf = []
            for i in range(0, len(word2index)):
                tf.append(0)
                
            for voca in token.keys():
                if voca in word2index.keys():
                    tf[word2index[voca]] += token[voca]
                if voca not in word2index.keys():
                    #continue
                    fw = find_word_in_List(voca, list(word2index.keys()))
                    print("%s -> %s" % (voca, fw))
                    tf[word2index[fw]] += token[fw]
            tf_max = max(tf)
            if tf_max == 0:
                tf_max = 1
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
        idf = math.log10(len(TF) / num) + 0.000000000000000000000000000000001
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
'''
    # KeyWord
    input: Weight(Weight=TF*IDF, 형식: list([[],[],[],[],[]]), word2index(인덱싱한것, 형식: Dictionary(단어:index넘버))
    output: AllKeyword(문서별로 키워드 상위 5개 모음, 형식: list([[],[],[],[],[]])
    '''
def KeyWord(Weight, word2index):
    AllKeyword = []
    for weight in Weight:
        keyword = []
        rankIdx = list(np.argsort(np.array(weight)))
        rankIdx.reverse()
        
        for idx in range(0,5):
            for key, value in word2index.items():
                if value == rankIdx[idx]:
                    keyword.append(key)
        AllKeyword.append(keyword)
    return AllKeyword
