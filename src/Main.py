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
    위로드릴께요
    '''
query.append(PreprocessComment(query_text1))
#30대
query_text2 = '''
    ㄴㄴ 그 여자 걍 대마초 피고 술취해서 집 잘못 찾은거아니냐 콘도살아 집살아??
    '''
query.append(PreprocessComment(query_text2))
#10대
query_text3 = '''
    어느부분에서 심쿰해야하는걸까...흠...
    '''
query.append(PreprocessComment(query_text3))

query_tf = TF(indexing_list, query, 'query')
query_weight = Weighting(query_tf, idf_list)

for i in idf_list:
    if i == 0:
        print("0dklndsfnkls")

query_weight = Normalize(query_weight)
score = Scoring(weighting_list, query_weight)
rank = Ranking(score)
keyword = KeyWord(weighting_list, indexing_list)

print(keyword)
print(rank)
