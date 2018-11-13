from nltk.corpus import wordnet
from nltk import word_tokenize
import nltk
import glob
import re
import sys


pattern = re.compile("[A-Za-z0-9]+")
aspects = ["CLEANLINESS", "ROOMS", "LOCATION", "SERVICE", "VALUE", "OTHER", "FOOD"]
final_list = []
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

for i in range(0, len(aspects)):
    filename = "/home/yash/Desktop/miniproject/all" + str(aspects[i]) + ".txt"
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
def extra(sentence):
    wordslist = word_tokenize(sentence.lower())
    tagged = nltk.pos_tag(wordslist)
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
                               for j in range(0,7):
                                   if phrase in switcher.get(j):
                                       nouns.append((phrase,j))
                                       mark[i] = 0
                                       mark[i+1] = 0
                                       break

    for i in range(0, len(tagged)):
        if mark[i] == 1:
            m = re.match(pattern, tagged[i][0])
            if m:
                if len(tagged[i][0]) > 2:
                    if tagged[i][1][0] == 'N':
                        for j in range(0, 7):
                            if tagged[i][0] in switcher.get(j):
                                nouns.append((tagged[i][0],j))
                                break

    for i in range(0, len(tagged)):
        m = re.match(pattern, tagged[i][0])
        if m:
            if len(tagged[i][0]) > 2:
                if tagged[i][1][0] == 'J' or tagged[i][1][0] == 'R':
                    adjs.append(tagged[i][0])
    return (nouns,adjs)

#
# sene = "we went to the steak house (la cava) and it was great"
# a,b = extra(sene)
#
# print(a)
# print(b)
#
