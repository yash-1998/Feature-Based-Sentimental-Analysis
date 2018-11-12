from nltk.corpus import  wordnet
from nltk import word_tokenize
import nltk
import glob
import re
pattern = re.compile("[A-Za-z0-9]+")
fileList =glob.glob('/home/yash/Desktop/miniproject/finalreviews/*.txt')
fileList.sort()
i=1
aspects = ["CLEANLINESS","ROOMS","LOCATION","SERVICE","VALUE","OTHER","FOOD"]
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
    filename = "/home/yash/Desktop/miniproject/all"+str(aspects[i])+".txt"
    with open(filename, 'r') as myfile:
        while True:
            data = myfile.readline()
            if not data:
                break
            temp1 = data.split(',')
            temp2 = temp1[0].split('\'')
            word = temp2[1]
            print(data)
            print(word)
            switcher.get(i).append(word)

sentencenounlist = []
for filename in fileList:
    print(i)
    temp1 = filename.split("/home/yash/Desktop/miniproject/finalreviews/review_")
    temp2 = temp1[1].split(".txt")
    index = temp2[0]
    with open(filename, 'r') as myfile:
        data = myfile.read().replace('\n', '')
        sentences = data.split('.')

        for sentence in sentences:
            particularsentence = []
            wordslist = word_tokenize(sentence.lower())
            tagged = nltk.pos_tag(wordslist)
            ft=False
            features=[]
            opinionwords=[]
            for t in tagged:
                m = re.match(pattern, t[0])
                if m:
                    if len(t[0]) > 2:
                        if t[1][0] == 'N':
                            for i in range(0,6):
                                if t[0] in switcher.get(i):
                                    features.append(t[0])
                                    ft=True

            for t in tagged:
                m = re.match(pattern, t[0])
                if m:
                    if len(t[0]) > 2:
                        if t[1][0] == 'J' or t[1][0] == 'R':
                            opinionwords.append(t[0])


