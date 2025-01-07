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

class Privileges:
    def __init__(self, privileges):
        self.privileges = privileges

    def show_privileges(self):
        print(f"権限:")
        if self.privileges[0] == "1":
            print("記事を追加できる")
        if self.privileges[1] == "1":
            print("記事を削除できる")
        if self.privileges[2] == "1":
            print("ユーザーを管理できる")
        if self.privileges == "000":
            print("権限がありません")


class Admin(User):
    def __init__(self,first_name,last_name,age,password,privileges,login_attempts = 0):
        super().__init__(first_name,last_name,age,password,login_attempts)
        if privileges in ["111","110","101","001","011","000"]:
            self.privileges = Privileges(privileges)  # Privilegesインスタンス
        else:
            raise ValueError("権限には111,110,101,001,011,000のいずれかを指定してください。")

    def show_privileges(self):
        print(f"対象者:{self.last_name} {self.first_name}")
        self.privileges.show_privileges()

taro = User("Taro","Yamada",32,"password")
sato = User("Tomoki","Sato",23,"p@Ssw0rd")
hanako = User("Hanako","Tanaka",25,"112233")
masaki = Admin("Masaki","Tanaka",24,"root","111")
tasaki = Admin("Maya","Tasaki",24,"ro0ot","011")

masaki.show_privileges()
tasaki.show_privileges()