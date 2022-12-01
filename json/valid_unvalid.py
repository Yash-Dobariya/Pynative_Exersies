import json


   
company="""{ 
   "company":{ 
      "employee":{ 
         "name":"emma",
         "payble":{ 
            "salary":7000,
            "bonus":800
         }
      }
   }
}"""

valid=json.dumps(company)
print(valid)

# secound method

# echo { "company":{ "employee":{ "name":"emma", "payble":{ "salary":7000 "bonus":800} } } } | python -m json.too