#  Access the value of key2 from the following JSON

import json

sampleJson = """{"key1": "value1", "key2": "value2"}"""

access_value=json.loads(sampleJson)
print(access_value['key2'])

