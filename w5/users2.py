class User:
    def __init__(self,first_name,last_name,age,password,login_attempts = 0):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.password = password
        self.login_attempts = login_attempts

    def describe_user(self):
        print(f"{self.last_name} {self.first_name}さんの年齢は{self.age}歳です。パスワードは{self.password}で、試行回数は{self.login_attempts}回です。")

    def greet_user(self):
        print(f"ようこそ、{self.last_name} {self.first_name}さん！")

    def increment_login_attempts(self):
        self.login_attempts += 1

    def reset_login_attempts(self):
        self.login_attempts = 0