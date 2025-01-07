cities = {
    "東京": {"国":"日本", "人口":"約1400万人", "事実":"秋葉原がある。"},
    "ニューヨーク": {"国": "アメリカ", "人口": "約840万人", "事実": "自由の女神がある。"},
    "パリ": {"国": "フランス", "人口": "約210万人", "事実": "エッフェル塔がある。"}
}

for name, date in cities.items():
    kuni = date.get("国")
    jinko = date.get("人口")
    jijitu = date.get("事実")
    print(f"{name}:所属-{kuni},人口 - {jinko},マメ知識 - {jijitu}")
    print()