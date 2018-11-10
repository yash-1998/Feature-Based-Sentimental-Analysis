import pandas
import sys

sys.stdout = open('file.txt', 'w')
df1 = pandas.read_csv('data1.csv')
df2 = pandas.read_csv('data2.csv')
df3 = pandas.read_csv('data3.csv')


def convert(x):
    newx = x.split('.,')
    s = ''
    for i in range(len(newx)-1):
        s = s + newx[i] + '.'
    s = s + newx[len(newx)-1]
    return s


count = 1
for i in range(len(df1['segments'])):
    df1.at[i, 'segments'] = convert(df1['segments'][i])
    print(count)
    print(df1['segments'][i])
    count = count + 1


for i in range(len(df2['segments'])):
    df2.at[i, 'segments'] = convert(df2['segments'][i])
    print(count)
    print(df2['segments'][i])
    count = count + 1

for i in range(len(df3['segments'])):
    df3.at[i, 'segments'] = convert(df3['segments'][i])
    print(count)
    print(df3['segments'][i])
    count = count + 1

