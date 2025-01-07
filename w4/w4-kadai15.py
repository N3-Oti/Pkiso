def city_country(name,kuni):#都市国titleで返す
    kaeri = f"{name},{kuni}"
    return kaeri.title()

test = city_country("kobe","japan")
print(f"1:{test}")
test2 = city_country("nagoya","japan")
print(f"2:{test2}")
test3 = city_country("tairen","china")
print(f"3:{test3}")