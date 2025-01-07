import json

filename = "./w4/num.json"
try:
    x = int(input("好きな数字を入力してください:"))
    with open(filename, "w", encoding='utf-8') as file_obj:
        json.dump(x,file_obj)

    with open(filename, encoding='utf-8') as file_obj2:
        num = json.load(file_obj2)
    print(f"あなたの好きな番号を知っています ! それは{num}です。")

except ValueError:
    print("数字を入力してください。")