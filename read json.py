import json
import sys

with open("read.json", 'r') as file:
    data = json.load(file)

content = json.loads(file)

file.close()
