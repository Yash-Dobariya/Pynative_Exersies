# Sort JSON keys in and write them into a file
import json

sampleJson = {"id" : 1, "name" : "value2", "age" : 29}

load= json.loads(sampleJson,indent=2, separators=(",", " = "))
print(load)