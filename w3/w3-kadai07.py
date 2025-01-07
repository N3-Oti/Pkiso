favorite_places = {
    "taro":["nagoya","oosaka","tokyo"],
    "mio":["yama","kawa","umi"],
    "hanako":["kyoto","iwate","hyogo"]
}

for name, basyo in favorite_places.items():
    for j in basyo:
        print(f"{name}が好きな場所は{j}です。")
    print()