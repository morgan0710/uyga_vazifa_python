#Quyidagi ma’lumotdan har bir o‘quvchining o‘rtacha bahosini hisoblang.

students = {
    "Ali": [80, 90, 85],
    "Vali": [70, 60, 75],
    "Sami": [95, 88, 92]
}
for ism, son in students.items():
    average = sum(son) / len(son)
    print(f"{ism}: {average:.1f}")

# Narxi 100 dan katta bo‘lgan mahsulotlarni chiqaring.

products = [
    {"name":"olma", "price":120},
    {"name":"anor", "price":90},
    {"name":"banan", "price":150}
]
for product in products:
    if product["price"] > 100:
        print(f"{product['name']} qimmat: {product['price']}")

# 18 yoshdan katta foydalanuvchilarni chiqaring.

users = [
    {"name":"Ali", "age":20},
    {"name":"Vali", "age":16},
    {"name":"Sami", "age":25}
]
for user in users:
    if user["age"] > 18:
        print(f"{user['name']}: {user['age']}")

# Har bir kursdagi o‘quvchilar sonini aniqlang.

courses = {
    "python": ["Ali","Vali","Sami"],
    "django": ["Ali","Sami"],
    "ai": ["Vali","Sami","Jasur"]
}
for course in courses.keys():
    print(f"{course}: {len(courses[course])}")


# Eng katta sonni toping:

numbers = [
    [4,7,2],
    [9,1,5],
    [3,8,6]
]
for row in numbers:
    print(max(row))

#Faqat active foydalanuvchilarni chiqaring.

data = {
    "users":[
        {"name":"Ali", "active":True},
        {"name":"Vali", "active":False},
        {"name":"Sami", "active":True}
    ]
}
for user in data["users"]:
    if user["active"]:
        print(user["name"])