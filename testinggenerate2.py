import json
import sys


sys.stdout = open('optimization.txt','w')
with open('beauty1.json', 'r') as f:
    review = json.load(f)

aspect = "NOTRELATED"
base = "/home/yash/Desktop/miniproject/finalreviews/review_"
test_base = "/home/yash/Desktop/miniproject/testvalues2/review_"
aspects = ["ROOMS", "LOCATION", "SERVICE", "VALUE", "FOOD"]
pp = []
jj=74
for i in range(74,220):
    pp.append(jj)
    jj=jj+8
i=1
c=1
for x in review:
    if i not in pp:
        print(c)
        file = open(test_base + str(c) + ".txt", "w")
        reviewfile = open(base+str(c)+".txt","r")
        data = reviewfile.read().replace('\n', '')
        sentences = data.split('.')
        dic = {}
        dic["ROOMS"]=0
        dic["SERVICE"]=0
        dic["LOCATION"]=0
        dic["FOOD"]=0
        dic["VALUE"]=0

        for j,k in zip(x['segmentLabels'],x['segments']):
            kk = k.encode('ascii','ignore')
            kkk = kk.replace('.',' ')
            kkk = kkk.lower()
            # print(kkk)
            # print(sentences)
            if kkk in sentences:
                for jj in j:
                    # print(jj + " " + j[jj])
                    if jj in aspects:
                        if j[jj] == 'p':
                            dic[jj.encode('ascii','ignore')]=dic[jj.encode('ascii','ignore')] + 1
                        if j[jj] == 'n':
                            dic[jj.encode('ascii','ignore')]=dic[jj.encode('ascii','ignore')] - 1
        for aspect in aspects:
            file.write(aspect + " " + str(dic[aspect]) + "\n")
        c=c+1
    i=i+1
