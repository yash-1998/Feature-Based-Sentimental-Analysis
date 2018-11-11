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



with open('beauty1.json', 'r') as f:
    review = json.load(f)

aspect = "NOTRELATED"
base = "/home/yash/Desktop/miniproject/finalreviews/review_"
i=1

for x in review:
    file = open(base+str(i) + ".txt","w")
    for j,k in zip(x['segmentLabels'],x['segments']):
        if len(j)>0 and aspect not in j:
            temp = k.encode('ascii','ignore').replace('.',' ')
            sentence = temp.encode('ascii', 'ignore').replace('!', ' ')
            file.write(sentence.lower() + '.')
    i=i+1