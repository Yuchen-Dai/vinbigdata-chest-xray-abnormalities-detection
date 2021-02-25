import csv, os, random

inFile = "train.csv"
trainFile = "data/train.txt"
valFile = "data/val.txt"
#   image_id,class_name,class_id,rad_id,x_min,y_min,x_max,y_max

with open(inFile, 'r') as csvInFile:
    dict_reader = csv.DictReader(csvInFile, delimiter=',')
        # csvWriter = csv.DictWriter(csvTrainFile, fieldnames = ['x_min','y_min','x_max','y_max','class_id'])
    outText = []
    seenImageId = {}

    for orderedDict in dict_reader:
        inDict = dict(orderedDict)
        inDict["class_id"] = int(inDict["class_id"])
        if inDict["class_id"] == 14: # = 14: No abnomality
            inDict["x_min"] = 0.0
            inDict["x_max"] = 0.0
            inDict["y_min"] = 0.0
            inDict["y_max"] = 0.0
            continue

        if inDict["image_id"] not in seenImageId:
            outText.append(f"{inDict['image_id']}.jpg {inDict['x_min']},{inDict['y_min']},{inDict['x_max']},{inDict['y_max']},{inDict['class_id']}")
            seenImageId[inDict["image_id"]] = outText.index(outText[-1])
        else:
            idx = seenImageId[inDict['image_id']]
            outText[idx] = outText[idx] + f" {inDict['x_min']},{inDict['y_min']},{inDict['x_max']},{inDict['y_max']},{inDict['class_id']}"
# random.seed(0)
random.shuffle(outText)

imageNum = len(outText)
# imageNum = 12
trainNum = round(0.75 * imageNum)
valNum = imageNum - trainNum

with open(trainFile, 'w') as csvtrainFile:
    with open(valFile, 'w') as csvValFile:
        for i in outText:
            if trainNum != 0:
                trainNum-=1
                csvtrainFile.write(i+"\n")
            # elif valNum != 0:
            #     valNum -= 1
            #     csvValFile.write(i+"\n")
            else:
                csvValFile.write(i+'\n')





        