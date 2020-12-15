import gzip
import gensim 
import pandas as pd
import numpy as np
import csv
import os
import re
import jsonify

data = pd.read_csv("tweets.csv",index_col=0)

# preprocess using gensim.utils.simple_preprocess function
data['text_preprocessed'] = data['text'].apply(lambda x: gensim.utils.simple_preprocess(x))

# build vocabulary and train model
model = gensim.models.Word2Vec(
    data['text_preprocessed'].tolist(),
    size=150,
    window=10,
    min_count=2,
    workers=-1,
    iter=10)

# Done building the model, let's look at some results
def phrase(sen):

    wordList = re.sub("[^\w]", " ",  sen).split() 
    result = []
    for w  in wordList:
        result.extend(model.wv.most_similar(positive=w))
    mot=[]
    for i in range(0,len(result)):
         mot.append(result[i][0])
    np.savetxt(r'np1.txt', data['text'].values, fmt='%s',encoding="utf8")
    with open('np1.txt', 'r',encoding="utf8" ) as f:
          raw_data = f.read()
    
    list_line=[]
    list_line=raw_data.split('\n')
    list_result=[]
    list_word= []
    for j in range(0,len(list_line)):
          list_word=list_line[j].split(' ')
          for k in range(0,len(mot)):
                  for h in range(0,len(list_word)):
                         if mot[k] == list_word[h]:
                                  list_result.append(list_line[j])

  
    return str(list_result)

def isWordInSentence(sen, phrase):
    s = sentence.split(" ")
    for i in s:
        if (i == word):
            return True
    return False