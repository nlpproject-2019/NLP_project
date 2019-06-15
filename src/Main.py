#-*- coding:utf-8 -*-
from WordWeighting import *
from preprocessing import *
from Ranking import *
from list import *

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

# variables
f = open('../test_data/test_50.txt', 'rt', encoding='UTF8')
count = 0
result = 0

keyword = KeyWord(weighting_list, indexing_list)

for ageKeyword in keyword:
    print(ageKeyword)

while True:
    # query variables
    query = []
    query_tf = []
    query_weight = []
    query_text1 = f.readline().rstrip('\n')
    print(query_text1)
    if not query_text1:
        break
    query.append(PreprocessComment(query_text1))
    query_tf = TF(indexing_list, query, 'query')
    query_weight = Weighting(query_tf, idf_list)


    query_weight = Normalize(query_weight)
    score = Scoring(weighting_list, query_weight)
    rank = Ranking(score)
    print(rank)
    print("")
    
    count += 1
    for r in rank:
        if(str(list(r.keys())[0]) == '10대'):
            result += 1
    
    
    

print("전체 댓글 : %d " % count)
print("결과 : %d " % result)
print("정확도 : %f" % (result/count))
