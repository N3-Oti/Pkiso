def build_profile(first, last, **user_info):#ユーザーに関する情報を含む辞書を作成
    user_info['first_name'] = first
    user_info['last_name'] = last
    return user_info

my_profile = build_profile("Hidehiro","Kajiya",
                            location="Nagoya",
                            school="KIC",
                            Grade="M1")

print(f"私の名前は{my_profile["last_name"]} {my_profile["first_name"]}で、{my_profile["location"]}に住んでいます。\n{my_profile["school"]}所属で学年は{my_profile["Grade"]}です。")
