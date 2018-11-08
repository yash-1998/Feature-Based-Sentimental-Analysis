import pandas
import sys
import json
import nltk
from nltk.corpus import stopwords 
from nltk.tokenize import word_tokenize, sent_tokenize 
stop_words = set(stopwords.words('english')) 


sys.stdout = open('file.txt', 'w')

with open('beauty1.json', 'r') as f:
    review = json.load(f)

i=1
nountags = ['NN','NNS','NNP','NNPS']
adjectivetags = [ 'JJ' , 'JJR' , 'JJS']
nouns=open("/home/yash/Desktop/miniproject/nouns.txt",'w')
adjectives=open("/home/yash/Desktop/miniproject/adjectives.txt",'w')

for x in review:
    print(i)
    for j,k in zip(x['segmentLabels'],x['segments']):
        if  "ROOMS" in j and len(j)==1:
            print(j)
            print(k.encode('ascii','ignore'))
            tokenized = sent_tokenize(k)
            for ii in tokenized: 
                # Word tokenizers is used to find the words  
                # and punctuation in a string 
                pretag = nltk.word_tokenize(ii) 
                tagged = nltk.pos_tag(pretag) 
                #print(tagged) 
                for item in tagged:
                    word,grammar = item
                    if grammar in nountags: 
                        print("noun = " + word.encode('ascii','ignore'))
                        nouns.write(word.encode('ascii','ignore'))
                        nouns.write("\n") 
                    if grammar in adjectivetags: 
                        print("adjective = " +word.encode('ascii','ignore'))
                        adjectives.write(word.encode('ascii','ignore'))
                        adjectives.write("\n")  
                    

            print("**********************************")

    print
    i=i+1

