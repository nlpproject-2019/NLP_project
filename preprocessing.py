import math
import time
import numpy as np

from collections import Counter
from konlpy.tag import Okt 
okt=Okt()

# (전처리) 길이가 2이상인 명사만 고르기
def get_nouns(text):
    nouns = okt.nouns(text)
    nouns = [word for word in nouns if len(word) > 1]
    return nouns

wordbox = []

file = open("input/10.txt", 'r', encoding='UTF8')
doc = file.read()
file.close()
token = get_nouns(doc)
wordbox.append(Counter(token))

file = open("input/20.txt", 'r', encoding='UTF8')
doc = file.read()
file.close()
token = get_nouns(doc)
wordbox.append(Counter(token))

file = open("input/30.txt", 'r', encoding='UTF8')
doc = file.read()
file.close()
token = get_nouns(doc)
wordbox.append(Counter(token))

file = open("input/40.txt", 'r', encoding='UTF8')
doc = file.read()
file.close()
token = get_nouns(doc)
wordbox.append(Counter(token))

file = open("input/50.txt", 'r', encoding='UTF8')
doc = file.read()
file.close()
token = get_nouns(doc)
wordbox.append(Counter(token))