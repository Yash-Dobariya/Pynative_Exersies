# PrettyPrint following JSON data

import json
pretty_data = {"id" : 1, "name" : "value2", "age" : 29}
print("Started writing JSON data into a file")
with open("pretty_data.json", "w") as write_file:
    json.dump(pretty_data, write_file, indent=4, sort_keys=True)
print("Done writing JSON data into a file")