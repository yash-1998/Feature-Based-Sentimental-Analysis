file1 = open("/home/yash/Desktop/miniproject/allrooms.txt","w")
file2 = open("/home/yash/Desktop/miniproject/alllocation.txt","w")
file3 = open("/home/yash/Desktop/miniproject/allvalue.txt","w")
file4 = open("/home/yash/Desktop/miniproject/allcleanliness.txt","w")
file5 = open("/home/yash/Desktop/miniproject/allfood.txt","w")
file6 = open("/home/yash/Desktop/miniproject/allother.txt","w")


fr = open("/home/yash/Desktop/miniproject/allfeatures.txt", "r")
while True:
    line = fr.readline()
    if not line:
        break
    print(line)
    x = raw_input()
    if x ==  '1':
        file1.write(line)
        print("written in rooms")
    if x ==  '2':
        file2.write(line)
        print("written in location")
    if x ==  '3':
        file3.write(line)
        print("written in value")
    if x ==  '4':
        file4.write(line)
        print("written in cleanliness")
    if x ==  '5':
        file5.write(line)
        print("written in food")
    if x ==  '6':
        file6.write(line)
        print("written in others")
    if x ==  '7':
        file6.write(line)
        print("written in services")
    if x == '9' :
        print("discarded")