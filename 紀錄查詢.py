import csv 
from collections import Counter


with open('baseball.csv') as infile:
    data = list(csv.DictReader(infile))
    result = []
    for i in data:
        if int(i["home run"]) >= 10 and int(i["stral base"]) >= 10:
            result.append(i)


counts = Counter([i["name"] for i in result])
print('toatal',len(counts),"people actived this recored")
for r, p in enumerate(counts.most_common(3)):
    name, times = p[0], p[1]
    print(r+1, " places ", name ,"got it ",times, )
    for i in result:
        if i["name"] == name:
            print(name,i["year"],i['home run'],i["stral base"] )


