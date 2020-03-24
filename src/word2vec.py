from gensim.models import Word2Vec
from konlpy.tag import Okt
twitter = Okt()

def make_corpus_rm_stopwords(text):
    corpus = []
    for s in text.split('\n'):
        corpus.append(['/'.join(p) for p in twitter.pos(s, norm=True, stem=False) if p[1] == "Noun" or p[1] == "KoreanParticle"])
    return corpus

def skip_gram_model(corpus):
    model = Word2Vec(corpus, size=100, window=3, min_count=1, workers=4, iter=1000, sg=1, sample=1e-3)
    words = model.wv.index2word
    vectors = model.wv.vectors
    skip_gram_model_result = dict(zip(words, vectors))
    return model

def CBOW_model(corpus):
    model = Word2Vec(corpus, size=100, window=3, min_count=1, workers=4, iter=1000, sample=1e-3)
    words = model.wv.index2word
    vectors = model.wv.vectors
    CBOW_model_model_result = dict(zip(words, vectors))
    return model


f = open('../input/10.txt', 'r', encoding='UTF8')
text = ""
time = 0

while time < 500:
    text += f.readline()
    time += 1
f.close()

corpus10 = make_corpus_rm_stopwords(text)
skip_gram_model_1 = skip_gram_model(corpus10)
CBOW_model_1 = CBOW_model(corpus10)


f = open('../test_data/test_10.txt', 'r', encoding='UTF8')
test_text = ""
time = 0

while time < 10:
    test_text += f.readline()
    time += 1
f.close()

def make_corpus_rm_stopwords_for_test(text):
    corpus = []
    result = []
    for s in text.split('\n'):
        corpus.append([str(p[0] + '/' + p[1]) for p in twitter.pos(s, norm=True, stem=False) if p[1] == "Noun" or p[1] == "KoreanParticle"])

    for wordbox in corpus:
        if len(wordbox) != 0:
            result.extend(wordbox)
    return result

test_corpus = make_corpus_rm_stopwords_for_test(test_text)
# for word in test_corpus:
#     print(skip_gram_model_1.most_similar(word,topn= 2))
#     print(CBOW_model_1.most_similar(word, topn= 2))
#     print(type(CBOW_model_1.most_similar(word, topn= 2)))
#
#     break
print(skip_gram_model_1.most_similar('바보/Noun', topn=5))