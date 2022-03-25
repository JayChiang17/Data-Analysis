from cProfile import label
import csv
import matplotlib.pyplot as plot



data = []
with open('students-scores.csv') as infile:
    text = infile.read().split()
    captions = text[0].split(',')
    for e in text[1:]:
        stu = e.split(',')
        scores = [float(sc) for sc in stu[1:]]
        data.append([stu[0] + scores])


for stu in data:
    name = stu[0]
    scores = stu[1:]
    plot.clf()
    plot.plot(scores, marker = 'o', label = 'Score')
    plot.title(name)
    plot.xticks(range(len(scores)), captions[1:])
    plot.xlabel('Items')
    plot.ylabel('Scores')
    plot.ylim(0,100)
    plot.tight_layout()
    plot.savefig(name + '.png')
    #plot.show()