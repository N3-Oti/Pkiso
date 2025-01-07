import random
age = random.randrange(100)
#age = 20
if age >= 65:
    print(f"{age}歳なので「高齢者」です。")
elif age >= 20:
    print(f"{age}歳なので「大人」です。")
elif age >= 13:
    print(f"{age}歳なので「少年」です。")
elif age >= 4:
    print(f"{age}歳なので「子供」です。")
elif age >= 2:
    print(f"{age}歳なので「幼児」です。")
else:
    print(f"{age}歳なので「赤ん坊」です。")