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
filew = open("/home/yash/Desktop/miniproject/dataset.tsv","w")
aspect = "ROOMS"
sentenceNounList=[]
for x in review:
    print(i)
    # os.mkdir("/home/yash/Desktop/miniproject/ReviewFolder/Review_" + str(i))
    #file=open("/home/yash/Desktop/miniproject/ReviewFolder/Review_" + str(i) + "/"+str(aspect)+"temp.txt",'a')
    for j,k in zip(x['segmentLabels'],x['segments']):
        if aspect in j and len(j)==1:
            print(j)
            #file.write(k.encode('ascii','ignore'))
            #file.write("\n")
            sentence = k.lower()
            tokenized = sent_tokenize(sentence)
            for ii in tokenized:
                # Word tokenizers is used to find the words
                # and punctuation in a string
                pretag = nltk.word_tokenize(ii)
                tagged = nltk.pos_tag(pretag)
                print(tagged)
                # for item in tagged:
                #     word,grammar = item
                #     if grammar in nountags:
                #         print("noun = " + word.encode('ascii','ignore'))
                #         nouns.write(word.encode('ascii','ignore'))
                #         nouns.write("\n")
                # Save only Noun tags in the "noun" list for further processing in each review sentence
                nouns = []
                for t in range(0,len(tagged)):
                    m = re.match(pattern,tagged[t][1])
                    if m:
                        if len(tagged[t][0])>2:
                            if tagged[t][1][0] == 'N':
                                nouns.append(tagged[t][0])

                for noun in nouns:
                    filew.write(noun+'\t')
                if len(nouns)!=0:
                    filew.write('\n')
            print("**********************************")
    print
    i=i+1
