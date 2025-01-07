def make_sand(guzai_list):
    if guzai_list:
        sandwich = ["パン"]
        sandwich.extend(guzai_list)
        sandwich.append("パン")
        print(f"サンドイッチ完成！：{sandwich}")
    else:
        print("具材が無い！")
    
guzai_list = []
while 1:
    guzai = input("挟みたい具材を入力してください（終了するにはqを入力してください）:")
    guzai = guzai.strip()
    if guzai == "q":
        break
    elif guzai:
        guzai_list.append(guzai)
    else:
        print("何も入力されていません。")

make_sand(guzai_list)