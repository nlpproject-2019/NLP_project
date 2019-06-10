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
tf_list = TF(indexing_list, tagged_list)
idf_list = IDF(tf_list)
weighting_list = Weighting(tf_list, idf_list)
weighting_list = Normalize(weighting_list)

# calculate query weighting
query_text = "저 국숭세간 졸업, 연봉 8000대, 개인 순자산 10억,"
query.append(PreprocessComment(query_text))

query_tf = TF(indexing_list, query)
query_weight = Weighting(query_tf, idf_list)

query_weight = Normalize(query_weight)
score = Scoring(weighting_list, query_weight)
rank = Ranking(score)

for i in rank:
    print(i)
