# File takes almost 3 mins.
# We have used NLTK standard pos_tag
# and not stanford tagger

import nltk
from nltk.util import ngrams

dict = {}
fr = open("data_preprocess.txt", "r")

gram_1_final = []
gram_2_final = []
gram_3_final = []
gram_4_final = []

while True:
    line = fr.readline()
    if not line:
        break

    comment = ''
    for i in range(len(line)):
        if line[i] == ' ':
            comment = line[i+1:]
            break

    comment_split = comment.split(".")
    for i in range(len(comment_split)):
        current_line = comment_split[i]
        tokenized = current_line.split()
        gram_1_list = ngrams(tokenized, 1)
        gram_2_list = ngrams(tokenized, 2)
        gram_3_list = ngrams(tokenized, 3)
        gram_4_list = ngrams(tokenized, 4)

        gram_1_final.extend(gram_1_list)
        gram_2_final.extend(gram_2_list)
        gram_3_final.extend(gram_3_list)
        gram_4_final.extend(gram_4_list)

print("Number of 1-gram features : " + str(len(gram_1_final)))
print("Number of 2-gram features : " + str(len(gram_2_final)))
print("Number of 3-gram features : " + str(len(gram_3_final)))
print("Number of 4-gram features : " + str(len(gram_4_final)))


for i in range(len(gram_1_final)):
    word = gram_1_final[i][0]
    temp = nltk.tag.pos_tag([word])
    if temp[0][1][0]=='N' :
        if word in dict:
            dict[word] = dict[word] + 1
        else:
            dict[word] = 0

for i in range(len(gram_2_final)):
    word = gram_2_final[i][0] + " " + gram_2_final[i][1]
    temp = nltk.tag.pos_tag([word])
    if temp[0][1][0]=='N' :
        if word in dict:
            dict[word] = dict[word] + 1
        else:
            dict[word] = 0

for i in range(len(gram_3_final)):
    word = gram_3_final[i][0] + " " + gram_3_final[i][1] + " " + gram_3_final[i][2]
    temp = nltk.tag.pos_tag([word])
    if temp[0][1][0]=='N' :
        if word in dict:
            dict[word] = dict[word] + 1
        else:
            dict[word] = 0

for i in range(len(gram_4_final)):
    word = gram_4_final[i][0] + " " + gram_4_final[i][1] + " " + gram_4_final[i][2] + " " + gram_4_final[i][3]
    temp = nltk.tag.pos_tag([word])
    if temp[0][1][0]=='N' :
        if word in dict:
            dict[word] = dict[word] + 1
        else:
            dict[word] = 0


sorted_dict = sorted(dict.items(), key=lambda kv: kv[1], reverse=True)
print(sorted_dict)



