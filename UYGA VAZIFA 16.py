import json

data = {"Model":"Malika", "Rang":"Qora", "Yil":2020, "Narh":40000}
data_json = json.dumps(data)
print(data_json)
print(type(data_json))

with open('data', 'w') as f:
    json.dump(data, f)

talaba_json = """{"ism":"Hasan","familiya":"Husanov","tyil":2000}"""
talaba = json.loads(talaba_json)
print(f"Ism: {talaba['ism']}\n Familiya: {talaba['familiya']}\n tyil: {talaba['tyil']}")

with open('talaba', 'w') as f:
    json.dump(talaba, f)


with open('students.json') as f:
    data = json.load(f)

for student in data['student']:
    print(f"{student['name']} {student['lastname']}, "
          f"{student['year']}-kurs, {student['faculty']} talabasi")