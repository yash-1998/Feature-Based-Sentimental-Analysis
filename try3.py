import glob

import nltk
from nltk import word_tokenize

from fp_growth import find_frequent_itemsets

import re


def unique(list1):
    unique_list = []
    for x in list1:
        if x not in unique_list:
            unique_list.append(x)
    return unique_list

def extractMax(input):
    numbers = re.findall('\d+', input)
    numbers = map(int, numbers)
    return max(numbers)

dict = {}
nounslist = []
for line in open("/home/yash/Desktop/miniproject/nouns.txt", 'r').readlines():
    nounslist.append([line.replace('\n','')])

print(len(nounslist))


npFile=open("/home/yash/Desktop/miniproject/ffeatures.txt",'w')

ffitemsets = find_frequent_itemsets(nounslist,10)

for itemset in ffitemsets:
    npFile.write(str(itemset)+'\n')
    itemstring = str(itemset)
    # print(itemstring)
    temp1 = itemstring.split(',')
    temp2 = temp1[0].split('\'')
    word = temp2[1]
    print(word)
    count = extractMax(itemstring)
    print(count)
    dict[word]=count
npFile.close()

#
# sorted_dict = sorted(dict.items(), key=lambda kv: kv[1], reverse=True)
#
# fileList =glob.glob('/home/yash/Desktop/miniproject/finalreviews/*.txt')
# fileList.sort()
# pattern = re.compile("[A-Za-z0-9]+")
# opinionlist= []
# i=1
# for filename in fileList:
#     print(i)
#     temp1 = filename.split("/home/yash/Desktop/miniproject/finalreviews/review_")
#     temp2 = temp1[1].split(".txt")
#     index = temp2[0]
#     with open(filename, 'r') as myfile:
#         data = myfile.read().replace('\n', '')
#         sentences = data.split('.')
#         for sentence in sentences:
#             wordslist = word_tokenize(sentence.lower())
#             tagged = nltk.pos_tag(wordslist)
#
#             # for ii in range(0, len(wordslist) - 1):
#             #     taglist = []
#             #     for j in range(0, ii):
#             #         taglist.append(wordslist[j])
#             #     concat = wordslist[ii] + " " + wordslist[ii + 1]
#             #     taglist.append(concat)
#             #     for j in range(ii + 2, len(wordslist)):
#             #         taglist.append(wordslist[j])
#             #     tagged = nltk.pos_tag(taglist)
#             op=False
#             for t in tagged:
#                 m = re.match(pattern, t[0])
#                 if m:
#                     if len(t[0]) > 2:
#                         if t[1][0] == 'N' and t[0] in dict:
#                             op=True
#             if op:
#                 for t in tagged:
#                     m = re.match(pattern, t[0])
#                     if m:
#                         if len(t[0]) > 2:
#                             if t[1][0] == 'J':
#                                 opinionlist.append(t[0])
#     i=i+1
#
# uniqueopinionlist = unique(opinionlist)
#
# opfile = open("/home/yash/Desktop/miniproject/opinionwords.txt","w")
# for word in uniqueopinionlist:
#     opfile.write(word+"\n")

pattern = re.compile("[A-Za-z0-9]+")

fileList =glob.glob('/home/yash/Desktop/miniproject/finalreviews/*.txt')
fileList.sort()
i=1
sentencenounlist = []
for filename in fileList:
    print(i)
    temp1 = filename.split("/home/yash/Desktop/miniproject/finalreviews/review_")
    temp2 = temp1[1].split(".txt")
    index = temp2[0]
    file1 = open("/home/yash/Desktop/miniproject/finalopinion/review_" + str(index) + ".txt","w")
    with open(filename, 'r') as myfile:
        data = myfile.read().replace('\n', '')
        sentences = data.split('.')
        for sentence in sentences:
            particularsentence = []
            wordslist = word_tokenize(sentence.lower())
            tagged = nltk.pos_tag(wordslist)
            for ii in range(0, len(wordslist) - 1):
                taglist = []
                for j in range(0, ii):
                    taglist.append(wordslist[j])
                concat = wordslist[ii] + " " + wordslist[ii + 1]
                taglist.append(concat)
                for j in range(ii + 2, len(wordslist)):
                    taglist.append(wordslist[j])
                tagged = nltk.pos_tag(taglist)
                op=False
                for t in tagged:
                    m = re.match(pattern, t[0])
                    if m:
                        if len(t[0]) > 2:
                            if t[1][0] == 'N' and t[0] in dict:
                                nouns = []
                                nouns.append(t[0])
                                particularsentence.append(t[0])
                                sentencenounlist.append(nouns)
                                op=True
            particularsentence=unique(particularsentence)
            file1.write("nouns :: ")
            for word in particularsentence:
                file1.write(word + ",")
            particularsentence = []
            if op:
                wordslist = word_tokenize(sentence.lower())
                tagged = nltk.pos_tag(wordslist)
                for t in tagged:
                    m = re.match(pattern, t[0])
                    if m:
                        if len(t[0]) > 2:
                            if t[1][0] == 'J':
                                particularsentence.append(t[0])
                file1.write(" adjectives :: ")
                for word in unique(particularsentence):
                    file1.write(word + ",")
            file1.write("\n")
    i=i+1
print("DONE")