import json

with open("R01_test.json") as jsonFile:
    jsonObject = json.load(jsonFile)
    jsonFile.close()

print(jsonObject['report_type'])

for i in jsonObject['items']:
    print(i)
