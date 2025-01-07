pets = {
    "tiwawa": {"ani": "dog", "owner": "taro"},
    "mikecat": {"ani": "cat", "owner": "mio"},
    "sibadog": {"ani": "dog", "owner": "hanako"},
    "golden_retriever": {"ani": "dog", "owner": "emma"},
    "shiba_inu": {"ani": "dog", "owner": "hiro"},
    "toy_poodle": {"ani": "dog", "owner": "sakura"},
    "chihuahua": {"ani": "dog", "owner": "carlos"},
    "siamese_cat": {"ani": "cat", "owner": "sophia"},
    "bengal_cat": {"ani": "cat", "owner": "leo"},
    "russian_blue": {"ani": "cat", "owner": "natasha"},
    "scottish_fold": {"ani": "cat", "owner": "oliver"},
    "rabbit": {"ani": "rabbit", "owner": "mia"},
    "parrot": {"ani": "bird", "owner": "liam"}
}

bingo_book = []

for i ,date in pets.items():
    ani = date.get("ani","no_ani")
    owner = date.get("owner","no_owner")
    print (f"{i}は{ani}の一種です。飼い主は{owner}です。")
    if ani == "dog":
        print(f"{owner}はdog派なので味方です。")
    elif ani == "cat":
        bingo_book.append(owner)
    else:
        print(f"{owner}は中立です。")
    print()
print(f"リスト：{bingo_book}")