class user:
    def __init__(self, ism, foydalanuvchi_ismi, email):
        self.ism = ism
        self.foydal_ismi = foydalanuvchi_ismi
        self.email = email

    def get_info(self):
        return f"ism: {self.ism}, foydalanuvchining ismi: {self.foydal_ismi}, email: {self.email}"

user1 = user("alijon1994", "Alijon Valiyev", "alijon1994@gmail.com")
user2 = user("malika_pro","Malika Ahmedova", "m.ahmedova@mail.com")

print(user1.get_info())
print(user2.get_info())
