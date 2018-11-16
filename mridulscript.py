from nltk.corpus import wordnet
from nltk import word_tokenize
import nltk
import glob
import re
import sys


pattern = re.compile("[A-Za-z0-9]+")
aspects = [ "ROOMS", "LOCATION", "SERVICE", "VALUE", "FOOD"]
final_list = []
roomslist = []
locationlist = []
servicelist = []
valuelist = []
foodlist = []
switcher = {
    0: roomslist,
    1: locationlist,
    2: servicelist,
    3: valuelist,
    4: foodlist,
}

for i in range(0, len(aspects)):
    filename = "/home/yash/Desktop/miniproject/pruned/final" + str(aspects[i])
    with open(filename, 'r') as myfile:
        while True:
            data = myfile.readline()
            if not data:
                break
            temp1 = data.split(',')
            temp2 = temp1[0].split('\'')
            word = temp2[1]
            switcher.get(i).append(word)

# print(foodlist)
def extra(sentence,index):
    wordslist = word_tokenize(sentence.lower())
    tagged = nltk.pos_tag(wordslist)
    print(tagged)
    nouns = []
    mark = []
    adjs = []
    # print(tagged)
    for i in range(0,len(tagged)):
        mark.append(1)
    for i in range(0,len(tagged)):
        if mark[i] == 1:
            m = re.match(pattern, tagged[i][0])
            if m:
                if len(tagged[i][0]) > 2:
                    if tagged[i][1][0] == 'N':
                       if i+1 < len(tagged):
                           if tagged[i+1][1][0] == 'N':
                               phrase = tagged[i][0] + " " + tagged[i+1][0]
                               for j in range(0,5):
                                   if phrase in switcher.get(j):
                                       nouns.append((phrase,j,i))
                                       mark[i] = 0
                                       mark[i+1] = 0
                                       break

    for i in range(0, len(tagged)):
        if mark[i] == 1:
            m = re.match(pattern, tagged[i][0])
            if m:
                if len(tagged[i][0]) > 2:
                    if tagged[i][1][0] == 'N':
                        for j in range(0, 5):
                            if tagged[i][0] in switcher.get(j):
                                nouns.append((tagged[i][0],j,i))
                                break

    for i in range(0, len(tagged)):
        m = re.match(pattern, tagged[i][0])
        if m:
            if len(tagged[i][0]) > 2:
                if tagged[i][1][0] == 'J' or tagged[i][1][0] == 'R':
                    if i > 0 and tagged[i-1][0].lower() == 'not' or tagged[i-1][0].lower() == 'too' or (len(tagged[i-1][0]) >= 3 and tagged[i-1][0].lower()[len(tagged[i-1][0])-3:len(tagged[i-1][0])] == "n't"):
                        adjs.append((tagged[i][0],i,-1))
                    else:
                        adjs.append((tagged[i][0],i,1))
    if index == '2':
        print("hello")
    if index == '2':
        print (nouns )
    if index == '2':
        print(adjs)
    return (nouns,adjs,tagged)

#
# sene = "we went to the steak house (la cava) and it was great"
# a,b = extra(sene)
#
# print(a)
# print(b)
#
