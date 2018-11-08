import glob
import re
import nltk
from nltk import pos_tag, word_tokenize
import csv
import sys
import os
from fp_growth import find_frequent_itemsets

pattern = re.compile("[A-Za-z0-9]+")
sys.stdout = open('fextractionop.txt', 'w')

filelist=glob.glob("/home/yash/Desktop/miniproject/Reviewfiles/*.txt")
print "POS tagging..."
print "Extracting features..."

nountags = ['NN','NNS','NNP','NNPS']
for filename in filelist:
	print(filename)
	sentenceNounList=[]
	head, tail = os.path.split(filename)
	base=os.path.splitext(tail)[0]
	# print(head)  /home/yash/Desktop/miniproject/Reviewfiles
	# print(tail)	Review_31.txt
	# print(base)	Review_31
	posFile=open(head+"/POS tagged/"+base+".txt",'w')
	for line in open(filename,'r').readlines():
		tokens = word_tokenize(line)
		tags=pos_tag(tokens)
		nouns=[]
		# Save only Noun tags in the "noun" list for further processing in each review sentence
		for t in tags:
			m = re.match(pattern,t[0])
     			if m:
				if len(t[0])>2:
					posFile.write('\n'+str(t))	
					if t[1][0] == 'N':
						nouns.append(t[0])
                #Save all the Noun Tags in each Review File/Database in sentenceNounList	
		sentenceNounList.append(nouns)
	posFile.close()	

	with open(head+"/CSV/"+base+".csv", "w") as f:
		writer = csv.writer(f)
		writer.writerows(sentenceNounList)
	f.close()

	#Save the Frequent Noun Phrases in NounPhrases Folder for each Review File/Database
	npFile=open(head+"/NounPhrases/"+base+".txt",'w')
	
	#Find the frequent Noun Phrases in each Review File/Database
	for itemset in find_frequent_itemsets(sentenceNounList,3):
		npFile.write('\n'+str(itemset))	
	npFile.close()
