import json

MyFile = open("cdcData.json", "r")

Lines = MyFile.readlines()

for L in Lines:
    values = L.split()
    print(values)

