import pandas
import sys
import json
import os
import nltk
import re
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize, sent_tokenize
stop_words = set(stopwords.words('english')) 



with open('beauty1.json', 'r') as f:
    review = json.load(f)

aspect = "NOTRELATED"
base = "/home/yash/Desktop/miniproject/finalreviews/review_"
test_base = "/home/yash/Desktop/miniproject/testvalues/review_"

pp = []
jj=74
for i in range(74,220):
    pp.append(jj)
    jj=jj+8
i=1
c=1
for x in review:
    if i not in pp:
        file = open(base + str(c) + ".txt", "w")
        for j,k in zip(x['segmentLabels'],x['segments']):
            if len(j)>0 and aspect not in j:
                temp = k.encode('ascii','ignore').replace('.',' ')
                sentence = temp.encode('ascii', 'ignore').replace('!', ' ')
                file.write(sentence.lower() + '.')
        c=c+1
    i=i+1