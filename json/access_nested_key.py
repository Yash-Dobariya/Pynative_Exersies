import json

sampleJson = """{ 
   "compani":{ 
      "employee":{ 
         "name":"emma",
         "payble":{ 
            "salary":7000,
            "bonus":800
         }
      }
   }
}
"""

access_key=json.loads(sampleJson)
print(access_key['company']['employee']['payble']['salary'])