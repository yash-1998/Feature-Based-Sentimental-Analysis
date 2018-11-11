import nltk
from nltk import ngrams
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize, sent_tokenize


stop_words = set(stopwords.words('english'))

sentence = 'it was amazing, large bathroom, and a sunk-in living room it had everything we needed'
print(sentence.split())
n = 2

wordslist = word_tokenize(sentence)

print(wordslist)
tagged = nltk.pos_tag(wordslist)
print(tagged)
for i in range(0,len(wordslist)-1):
    taglist = []
    for j in range(0,i):
        taglist.append(wordslist[j])
    concat = wordslist[i]+" "+wordslist[i+1]
    taglist.append(concat)
    for j in range(i+2,len(wordslist)):
        taglist.append(wordslist[j])
    print(taglist)
    tagged = nltk.pos_tag(taglist)
    print(tagged)