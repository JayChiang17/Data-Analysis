import csv
from collections import Counter


result = []
with open("student-scores.csv") as infile:
    data = infile.read().split()
    for e in data[1:]: #Caz the array[0] is the title
        stu = e.split(",") 
        scores = {int(sc) for sc in stu[1:]} #transfer from string to int
        exams = scores[3]*0.2 + scores[4]*0.3 
        hw = sum(sorted(scores[0:3])[1:])/2
        final = round(hw*0.5+exams, 2)
        print(stu[0], scores,'avg HW',hw,"total avg", final)

        stu.append(final)
        result.append(stu)

with open('new-scores.csv', 'w') as outfile:
    outfile.write(data[0]+'total scores\n')
    for stu in result:
        outfile.write(','.join([str(e) for e in stu] + "\n")) # when use join, in the list MUST be "STRING"