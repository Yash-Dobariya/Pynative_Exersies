#  Access the value of key2 from the following JSON

import json

sampleJson = """{"key1": "value1", "key2": "value2"}"""

access_value=json.loads(sampleJson)

# if you write wrong key then "get" function is return None

print(access_value.get('key'))

