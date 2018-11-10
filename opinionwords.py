import pandas
import sys
import json
import os
import nltk
import re
from nltk.corpus import stopwords 
from fp_growth import find_frequent_itemsets
from nltk.tokenize import word_tokenize, sent_tokenize 
stop_words = set(stopwords.words('english')) 


sys.stdout = open('opinionop.txt','w')
with open('beauty1.json', 'r') as f:
    review = json.load(f)

nountags = ['NN','NNS','NNP','NNPS']
adjectivetags = [ 'JJ' , 'JJR' , 'JJS']


pattern = re.compile("[A-Za-z0-9]+")
i=1

opinionlist = []
for x in review:
    print(i)
    for j,k in zip(x['segmentLabels'],x['segments']):
        print(j)
        tokenized = sent_tokenize(k)
        for ii in tokenized: 
            pretag = nltk.word_tokenize(ii) 
            tagged = nltk.pos_tag(pretag) 
            print(tagged) 
            for t in range(0,len(tagged)):
                m = re.match(pattern,tagged[t][1])
                if m:
                    if len(tagged[t][0])>2:
                        if tagged[t][1][0] == 'J':
                            print(tagged[t][0] + " :: ")
                            opinionlist.append(tagged[t][0])
                            
        print("**********************************")
    print
    i=i+1
