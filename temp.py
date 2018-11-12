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

nountags = ['NN','NNS','NNP','NNPS']
adjectivetags = [ 'JJ' , 'JJR' , 'JJS']


pattern = re.compile("[A-Za-z0-9]+")
i=1
aspects = ["CLEANLINESS","ROOMS","LOCATION","SERVICE","VALUE","OTHER","FOOD"]
for aspect in aspects:
    sentenceNounList=[]
    for x in review:
        print(i)
        # os.mkdir("/home/yash/Desktop/miniproject/ReviewFolder/Review_" + str(i))
        #file=open("/home/yash/Desktop/miniproject/ReviewFolder/Review_" + str(i) + "/"+str(aspect)+"temp.txt",'a')
        for j,k in zip(x['segmentLabels'],x['segments']):
            if aspect in j:
                print(j)
                #file.write(k.encode('ascii','ignore'))
                #file.write("\n")
                tokenized = sent_tokenize(k.lower())
                for ii in tokenized:
                    pretag = nltk.word_tokenize(ii)
                    tagged = nltk.pos_tag(pretag)
                    print(tagged)
                    for t in range(0,len(tagged)):
                        m = re.match(pattern,tagged[t][1])
                        if m:
                            if len(tagged[t][0])>2:
                                if tagged[t][1][0] == 'N':
                                    nouns=[]
                                    nouns.append(tagged[t][0].encode('ascii','ignore'))
                                    sentenceNounList.append(nouns)
                                    if t+1<len(tagged) and tagged[t+1][1][0] == 'N':
                                        nouns=[]
                                        phrase = tagged[t][0] + " " + tagged[t+1][0]
                                        print("Phrases = " + phrase)
                                        nouns.append(phrase.encode('ascii','ignore'))
                                        sentenceNounList.append(nouns)
                print("**********************************")
        print
        i=i+1

    print(sentenceNounList)
    npFile=open("/home/yash/Desktop/miniproject/all"+str(aspect)+".txt",'w')
    for itemset in find_frequent_itemsets(sentenceNounList,4):
        npFile.write(str(itemset)+'\n')
    npFile.close()
