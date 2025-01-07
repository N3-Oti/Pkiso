yamada = {"name":"Yamada","age":32,"city":"tokyo"}
satou = {"name":"Satou","age":44,"city":"tokyo"}
kobayasi = {"name":"Kobayasi","age":21,"city":"kyoto"}
tijin = [yamada,satou,kobayasi]

for koitu in tijin:
    koitu_name = koitu.get("name","no name")
    koitu_age = koitu.get("age","no age")
    koitu_city = koitu.get("city","no city")
    print(f"{koitu_name}さんのデータ:年齢{koitu_age},{koitu_city}在住です。")