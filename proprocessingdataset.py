import pandas
import sys
import json
import nltk
from nltk.corpus import stopwords 
from nltk.tokenize import word_tokenize, sent_tokenize 
stop_words = set(stopwords.words('english')) 
from textblob import TextBlob
import glob
import os

with open('beauty1.json', 'r') as f:
    review = json.load(f)
i=1
for x in review:
    print("Opening review " + str(i))
    file=open("/home/yash/Desktop/miniproject/Reviewfiles/Review_" + str(i) + ".txt",'a')
    for j,k in zip(x['segmentLabels'],x['segments']):
        file.write(k.encode('ascii','ignore'))
        file.write("\n")
    print("done\n")
    i=i+1

