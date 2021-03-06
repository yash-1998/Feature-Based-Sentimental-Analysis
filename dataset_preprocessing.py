import sys
from nltk.stem import WordNetLemmatizer
from nltk import word_tokenize
from nltk.corpus import stopwords
stop = set(stopwords.words('english'))
lemmatizer = WordNetLemmatizer()


print(lemmatizer.lemmatize(""))

fr = open("file.txt", "r")
sys.stdout = open('data_preprocess.txt', 'w')
count = 1

while True:
    line = fr.readline()
    if not line:
        break

    comment = ''
    for i in range(len(line)):
        if line[i] == ' ':
            comment = line[i+1:]
            break

    list = ['!', ':', ';', '{', '}', '(', ')', '[', ']']
    comments_split = comment.split('.')
    final_comment = ""
    for i in range(len(comments_split)):
        inner_comment = ""
        for j in word_tokenize(comments_split[i]):
            if j not in stop and j not in list:
                word_after_lem = lemmatizer.lemmatize(j)
                inner_comment = inner_comment + word_after_lem + " "
        final_comment = final_comment + inner_comment + "."

    print(count)
    print(final_comment)
    count = count+1
