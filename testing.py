from nltk.corpus import wordnet
from nltk import word_tokenize
import nltk
import glob
import re
from mridulscript import extra
import sys

sys.stdout = open('mingo.txt', 'w')
pattern = re.compile("[A-Za-z0-9]+")
fileList = glob.glob('/home/yash/Desktop/miniproject/finalreviews/*.txt')
fileList.sort()
i = 1
aspects = ["ROOMS", "LOCATION", "SERVICE", "VALUE", "FOOD"]
final_list = []
roomslist = []
locationlist = []
servicelist = []
valuelist = []
foodlist = []
pos_op = set([])
neg_op = set([])

posi_file = open("/home/yash/Desktop/miniproject/positive-words.txt", "r")
nega_file = open("/home/yash/Desktop/miniproject/negg.txt", "r")


while True:
    word = posi_file.readline()
    if not word:
        break
    words = word.split("\n")
    word = words[0]
    pos_op.add(word)

while True:
    word = nega_file.readline()
    if not word:
        break
    words = word.split("\n")
    word = words[0]
    neg_op.add(word)



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

opifile = open("/home/yash/Desktop/miniproject/opifile.txt", "w")
for filename in fileList:

    print("-----------------------------------------------------------------")
    temp1 = filename.split("/home/yash/Desktop/miniproject/finalreviews/review_")
    temp2 = temp1[1].split(".txt")
    index = temp2[0]
    print(index)
    with open(filename, 'r') as myfile:
        data = myfile.read().replace('\n', '')
        sentences = data.split('.')
        score = [0, 0, 0, 0, 0]
        for sentence in sentences:
            sentence = sentence.replace(","," ,")
            sentence = sentence.replace(".", " .")
            sentence = sentence.replace("-", " -")
            sentence = sentence.replace(":", " :")
            print(sentence)
            features,b,postag = extra(sentence,index)
            opinions = []
            for i in b:
                if i[0] in pos_op:
                    opinions.append((i[0],1*(int)(i[2]),i[1]))
                if i[0] in neg_op:
                    opinions.append((i[0],-1*(int)(i[2]),i[1]))
            if len(features) > 0 and len(opinions) > 0:
                print(features)
                print(opinions)
                mark = []
                for x in opinions:
                    mark.append(0)
                print("\n")

                for feature in features:
                    prvs = (-1,-1,-1)
                    k = 0
                    for opinion in opinions:
                        if opinion[2] < feature[2] and mark[k] == 0:
                            prvs = opinion
                            i = k
                        k += 1

                    j = 0
                    next = (-1, -1, -1)
                    for opinion in opinions:
                        if opinion[2] > feature[2] and mark[j] == 0:
                            next = opinion
                            break
                        j += 1

                    if prvs[2] == -1 and next[2] == -1:
                        continue
                    if prvs[2] == -1:
                        score[feature[1]] += next[1]
                        mark[j] = 1
                        print(feature[0] + str(feature[1]) + " " + next[0] +"\n")
                        continue

                    if next[2] == -1:
                        score[feature[1]] += prvs[1]
                        mark[i] = 1
                        print(feature[0] + str(feature[1]) + " " + prvs[0] + "\n")
                        continue

                    if abs(feature[2] - next[2]) < abs(feature[2] - prvs[2]):
                        mark[j] = 1
                        print(feature[0] + str(feature[1]) + " " + next[0] + "\n")
                        score[feature[1]] += next[1]
                    else:
                        mark[i] = 1
                        print(feature[0] + " " + prvs[0] + "\n")
                        score[feature[1]] += prvs[1]

        xx = 0
        for aspect in aspects:
            print(aspect + " " + str(score[xx]) + "\n")
            xx += 1

        prediction = open("/home/yash/Desktop/miniproject/predictions/predict"+str(index)+".txt", "w")
        xx = 0
        for aspect in aspects:
            prediction.write(aspect + " " + str(score[xx]) + "\n")
            xx += 1