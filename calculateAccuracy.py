n = 0
d = 0
for i in range(1,201):
    original_file = open("/home/yash/Desktop/miniproject/testvalues/review_"+str(i)+".txt", "r")
    prediction_file = open("/home/yash/Desktop/miniproject/predictions/predict"+str(i)+".txt", "r")
    c = 0
    while c < 7:
        x = original_file.readline()
        y = prediction_file.readline()

        tx = x.split(' ')
        ty = y.split(' ')
        print(tx[0])
        if tx[0] == "SERVICE":
            # c +=1
            # continue
            print("here")
            if (int)(tx[1])*(int)(ty[1]) > 0:
                n += 1
            if (int)(tx[1]) == 0 and (int)(ty[1]) == 0:
                n += 1
            d += 1
        c += 1
print(n)
print(d)
print(n/d)
