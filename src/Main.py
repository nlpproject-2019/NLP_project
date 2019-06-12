#-*- coding:utf-8 -*-
from WordWeighting import *
from preprocessing import *
from Ranking import *
from list import *

# query variables
query = []
query_tf = []
query_weight = []

# docs rank variables
score = []
rank = []

# docs variables
indexing_list = {}
tf_list = []
idf_list = []
weighting_list = []

# calculate docs weighting
indexing_list = Indexing(tagged_list)
tf_list = TF(indexing_list, tagged_list, 'word')
idf_list = IDF(tf_list)
weighting_list = Weighting(tf_list, idf_list)
weighting_list = Normalize(weighting_list)

#30대
query_text1 = '''
    저 국숭세단 졸업, 연봉 8000대, 개인 순자산 10억,
    부모님 20-25 정도 재산 기재했은데, 가입 할 때 여자 조건으로 지거국or인서울 졸업,
    여자 연봉 따지진 않지만, 무난한 외모에 부모님 노후 보장 되어 있는 있는 분이면 괜찮다 했는데.
    받는 프로필 여자분들 외모는 그럭 저럭 괜찮은데, 다른 프로필 다 별로라 ㅠㅠ..
    '''
query.append(PreprocessComment(query_text1))
#30대
query_text2 = '''
    저 국숭세단 졸업, 연봉 8000대, 개인 순자산 10억,
    부모님 20-25 정도 재산 기재했은데, 가입 할 때 여자 조건으로 지거국or인서울 졸업,
    여자 연봉 따지진 않지만, 무난한 외모에 부모님 노후 보장 되어 있는 있는 분이면 괜찮다 했는데.
    받는 프로필 여자분들 외모는 그럭 저럭 괜찮은데, 다른 프로필 다 별로라 ㅠㅠ..
    '''
query.append(PreprocessComment(query_text2))
#10대
query_text3 = '''
    초6?그때가 진심 최악 여자애들도 몇몇은 나랑 싸운 애들이였고 남자애들은 그 때 우리 학교에서 섹드립 치고 문제있는 애들만 다 모은거라 진심 개구렸는데
    젤 괜찮은 건 지금 반이양
    '''
query.append(PreprocessComment(query_text3))


query_tf = TF(indexing_list, query, 'query')
query_weight = Weighting(query_tf, idf_list)

query_weight = Normalize(query_weight)
score = Scoring(weighting_list, query_weight)
rank = Ranking(score)
keyword = KeyWord(weighting_list, indexing_list)

print(keyword)
print(rank)
