from users2 import User

class Privileges:
    def __init__(self, privileges):
        self.privileges = privileges

    def show_privileges2(self):
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
        self.privileges.show_privileges2()