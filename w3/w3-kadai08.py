like_num = {"Yamada":[4,5,6],
            "Satou":[5,7,9],
            "Utida":[777,888,999],
            "Oda":[50,80,90]
            }

for name, num in like_num.items():
    for i in num:
        print(f"{name}さんが好きな数字は{i}です。")
    print()