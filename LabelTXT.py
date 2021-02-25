from os import getcwd
#from sklearn.model_selection import train_test_split
import json
import glob
import csv

wd = getcwd()
classes = ["Aortic enlargement","Atelectasis","Calcification","Cardiomegaly","Consolidation","ILD",
           "Infiltration","Lung Opacity","Nodule/Mass","Other lesion","Pleural effusion",
           "Pleural thickening", "Pneumothorax","Pulmonary fibrosis"]

inputFile = "train.csv"
outputFile = open("train.txt","w") 

labelDict = {}
with open(inputFile,'r') as data: 
   for x in csv.reader(data):
       tempDict = {}
       if x[0] in labelDict:
           labelDict[x[0]].append([x[4],x[5],x[6],x[7],x[2]])
       else:
           labelDict[x[0]] =[[x[4],x[5],x[6],x[7],x[2]]]

for key,value in labelDict.items():
    result = key + ' '
    for i in range(len(value)):
        result +=','.join(value[i])
        result += ' '
    result += '\n'
    outputFile.write(result)
outputFile.close()
