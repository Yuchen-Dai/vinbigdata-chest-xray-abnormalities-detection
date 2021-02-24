from os import getcwd
from sklearn.model_selection import train_test_split
import json
import glob

wd = getcwd()
classes = ["Aortic enlargement","Atelectasis","Calcification","Cardiomegaly"]