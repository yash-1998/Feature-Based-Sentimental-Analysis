import sys

from nltk.corpus import wordnet
sys.stdout = open('mingo2.txt', 'w')

opifile = open("/home/yash/Desktop/miniproject/opifile.txt", "r")
posi_file = open("/home/yash/Desktop/miniproject/positive-words.txt", "r")
nega_file = open("/home/yash/Desktop/miniproject/negg.txt", "r")
positive = []
negative = []
positive_syno = []
negative_syno = []
opinion_word = []

while True:
    word = posi_file.readline()
    if not word:
        break
    words = word.split("\n")
    word = words[0]
    positive.append(word)
    for syn in wordnet.synsets(word):
        positive_syno.append(syn.name())

while True:
    word = nega_file.readline()
    if not word:
        break
    words = word.split("\n")
    word = words[0]
    negative.append(word)
    for syn in wordnet.synsets(word):
        negative_syno.append(syn.name())

while True:
    word = opifile.readline()
    if not word:
        break
    words = word.split("\n")
    word = words[0]
    opinion_word.append(word)

print("Len pos " +str(len(positive)))
print("Len neg "+ str(len(negative)))
print(positive)

def orientationsearch() :
    for word in opinion_word:
        word = word.split("\n")
        word = word[0]
        for i in wordnet.synsets(word):
            if i.name() in positive_syno:
                positive.append(word)
                return

            if i.name() in negative_syno:
                negative.append(word)
                return

    return

orientationsearch()
print("Len pos " +str(len(positive)))
print("Len neg "+ str(len(negative)))
print(positive)

pos_file = open("/home/yash/Desktop/miniproject/positive-words.txt","w")
neg_file = open("/home/yash/Desktop/miniproject/negg.txt","w")

for i in positive:
    pos_file.write(i+"\n")
for i in negative:
    neg_file.write(i+"\n")

# posi_file.close()
# nega_file.close()




