
import numpy as np
from WordWeighting import TF, Weighting 
from WordWeighting import list_Indexing, word_TF, word_IDF, word_Weight
# 이걸 list.py에서 가져오도록 수정할 것.

##----------------------------------------------
## 실험용 # query_wordbox 넘겨받음
#from collections import Counter
#import math

#Query = Counter(['바', '사', '마', '가', '마', '나', '다', '라'])
#Query_wordbox = []
#Query_wordbox.append(Query)
##----------------------------------------------

#----------------------------------------------
# 실험용 # query_wordbox 넘겨받음
from collections import Counter
import math
from preprocessing import get_nouns
Query_txt = '''
저 국숭세단 졸업, 연봉 8000대, 개인 순자산 10억, 부모님 20-25 정도 재산 기재했은데, 가입 할 때 여자 조건으로 지거국or인서울 졸업, 여자 연봉 따지진 않지만, 무난한 외모에 부모님 노후 보장 되어 있는 있는 분이면 괜찮다 했는데. 받는 프로필 여자분들 외모는 그럭 저럭 괜찮은데, 다른 프로필 다 별로라 ㅠㅠ..
'''
Query = Counter(get_nouns(Query_txt))
Query_wordbox = []
Query_wordbox.append(Query)
#----------------------------------------------

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


def Scoring(word_Weight, query_Weight):
    Score = []
    for weight in word_Weight:
        score = 0
        for i in range(0, len(weight)):
            score += weight[i] * query_Weight[0][i]
        Score.append(score)
    return Score

def Ranking(Score):
    doc = ['10대', '20대', '30대', '40대', '50대']
    rankIdx = list(np.argsort(np.array(Score)))
    rankIdx.reverse()

    Rank = {}
    for idx in rankIdx:
        Rank[doc[idx]] = Score[idx]
    return Rank

query_TF = TF(list_Indexing, Query_wordbox)
query_Weight = Weighting(query_TF, word_IDF)
word_Weight = Normalize(word_Weight)
query_Weight = Normalize(query_Weight)
Score = Scoring(word_Weight, query_Weight)
Rank = Ranking(Score)
print(Score)
print(Rank)