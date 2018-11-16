n = 0
d = 0
fi = open("/home/yash/Desktop/miniproject/racc.txt", "w")

for i in range(1,201):
    original_file = open("/home/yash/Desktop/miniproject/testvalues/review_"+str(i)+".txt", "r")
    prediction_file = open("/home/yash/Desktop/miniproject/predictions/predict"+str(i)+".txt", "r")
    c = 0
    nn = 0
    dd = 0
    while c < 5:
        x = original_file.readline()
        y = prediction_file.readline()

        tx = x.split(' ')
        ty = y.split(' ')
        if True:
            if (int)(tx[1])*(int)(ty[1]) > 0:
                nn = nn+1
                n += 1
            if (int)(tx[1]) == 0 and (int)(ty[1]) == 0:
                n += 1
                nn =nn + 1
            d += 1
            dd =dd +1
        c += 1
    fi.write(str(i) + " " + str(nn) + "/" + str(dd) + "\n")
print(n)
print(d)
x = n*100
x = x/d
print(x)
