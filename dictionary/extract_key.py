# Write a Python program to create a new dictionary by extracting the mentioned keys from the below dictionary.


sample_dict = {
    "name": "Kelly",
    "age": 25,
    "salary": 8000,
    "city": "New york"}

# Keys to extract
keys = ["name", "salary"]


newDict = {keys: sample_dict[keys] for keys in keys}
print(newDict)