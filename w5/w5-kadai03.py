class User:
    def __init__(self,first_name,last_name,age,password):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.password = password

    def describe_user(self):
        print(f"{self.last_name} {self.first_name}さんの年齢は{self.age}歳です。パスワードは{self.password}です。")

    def greet_user(self):
        print(f"ようこそ、{self.last_name} {self.first_name}さん！")


taro = User("Taro","Yamada",32,"password")
sato = User("Tomoki","Sato",23,"p@Ssw0rd")
hanako = User("Hanako","Tanaka",25,"112233")

taro.describe_user()
sato.describe_user()
hanako.describe_user()

taro.greet_user()
sato.greet_user()
hanako.greet_user()







