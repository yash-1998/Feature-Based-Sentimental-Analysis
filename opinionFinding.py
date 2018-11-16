from nltk.corpus import  wordnet
from nltk import word_tokenize
import nltk
import glob
import re
import sys

sys.stdout = open('mingo.txt','w')
pattern = re.compile("[A-Za-z0-9]+")
fileList =glob.glob('/home/yash/Desktop/miniproject/finalreviews/*.txt')
fileList.sort()
i=1
aspects = ["CLEANLINESS","ROOMS","LOCATION","SERVICE","VALUE","OTHER","FOOD"]
final_list=[]
cleanlinesslist = []
roomslist = []
locationlist = []
servicelist = []
valuelist = []
otherlist = []
foodlist = []
switcher = {
    0: cleanlinesslist,
    1: roomslist,
    2: locationlist,
    3: servicelist,
    4: valuelist,
    5: otherlist,
    6: foodlist,
}

for i in range(0,len(aspects)):
    filename = "/home/yash/Desktop/miniproject/pruned/final"+str(aspects[i])
    with open(filename, 'r') as myfile:
        while True:
            data = myfile.readline()
            if not data:
                break
            temp1 = data.split(',')
            temp2 = temp1[0].split('\'')
            word = temp2[1]
            switcher.get(i).append(word)

opifile = open("/home/yash/Desktop/miniproject/opifile.txt","w")
for filename in fileList:

    temp1 = filename.split("/home/yash/Desktop/miniproject/finalreviews/review_")
    temp2 = temp1[1].split(".txt")
    index = temp2[0]
    print(index)
    with open(filename, 'r') as myfile:
        data = myfile.read().replace('\n', '')
        print(data)
        sentences = data.split('.')

        for sentence in sentences:
            wordslist = word_tokenize(sentence.lower())
            tagged = nltk.pos_tag(wordslist)
            ft=False
            opinionwords=[]
            for t in tagged:
                m = re.match(pattern, t[0])
                if m:
                    if len(t[0]) > 2:
                        if t[1][0] == 'N':
                            for i in range(0,6):
                                if t[0] in switcher.get(i):
                                    ft = True
                m = re.match(pattern, t[0])
                if m:
                    if len(t[0]) > 2:
                        if t[1][0] == 'J' or t[1][0] == 'R' :
                            opinionwords.append(t[0])

            if ft == False:
                opinionwords = []

            for t in opinionwords:
                if t not in final_list:
                    final_list.append(t)

            print(opinionwords)

        print("**************************************************")

for t in final_list:
    opifile.write(t+"\n")

