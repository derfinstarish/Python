# working with csv and json
## This script demonstrates how to read and write CSV and JSON files in Python.
### to read

# import csv
# with open('python.csv', 'r') as csv_file:
#     x = csv.reader(csv_file)
#     for i in x:
#         print(i)

# for dictionary

# import csv
# with open('python.csv', 'r') as csv_file:
#     x = csv.DictReader(csv_file)
#     for i in x:
#         print(i)

# import csv
# a = [
#     ['name','age'],['Jhon',20],['Alice',25]
# ]
# with open('a3.csv','w')as csvfile:
#     x = csv.writer(csvfile)
#     x.writerows(a)

# Json

# import json
# with open('python.json', 'r') as jsonfile:
#     x = json.load(jsonfile)
#     print(x['name'], x['time'])

import json
a = {
    'product': 'Laptop',
    'price': 70000
}
with open('python2.json', 'w') as jsonfile:
    json.dump(a, jsonfile, indent=3)