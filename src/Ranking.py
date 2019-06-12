#-*- coding:utf-8 -*-

import numpy as np
import math
'''
    # Normalize
    input: Weight(Weight=TF*IDF, 형식: list([[],[],[],[],[]])
    output: unit_Weight(단위벡터화한 Weight, 형식: list([[],[],[],[],[]])
    '''
def Normalize(Weight):
    unit_Weight = []
    for weight in Weight:
        unit_weight = []
        sum = 0
        for element in weight:
            sum += math.pow(element, 2)
        for element in weight:
            unit_weight.append(element / math.sqrt(sum))
        unit_Weight.append(unit_weight)
    return unit_Weight
'''
    # Scoring
    input: word_Weight(단위벡터화한 데이터셋의 Weight, 형식: list([[],[],[],[],[]]), word_Weight(단위벡터화한 Query의 Weight, 형식: list([[],[],[],[],[]])
    output: Score(각 나이대별 score값 = input 두개를 내적한 값, 형식: list([]))
    '''
def Scoring(word_Weight, query_Weight):
    AllScore = []
    for q_weight in query_Weight:
        Score = []
        for weight in word_Weight:
            score = 0
            for i in range(0, len(weight)):
                score += weight[i] * q_weight[i]
            Score.append(score)
        AllScore.append(Score)
    return AllScore
'''
    # Ranking
    input: Score(각 나이대별 score값 = input 두개를 내적한 값, 형식: list([]))
    output: Rank(score값이 높은 순서대로 나열한 것, 형식: Dictionary(나이대:score값))
    '''
def Ranking(AllScore):
    doc = ['10대', '20대', '30대', '40대', '50대']
    AllRank = []
    
    for Score in AllScore:
        rankIdx = list(np.argsort(np.array(Score)))
        rankIdx.reverse()
        
        Rank = {}
        for idx in rankIdx:
            Rank[doc[idx]] = Score[idx]
        AllRank.append(Rank)
return AllRank
