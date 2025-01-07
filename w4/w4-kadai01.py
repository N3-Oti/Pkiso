name = input("あなたの名前はなんですか？:")
name = name.strip()

if name:
    filename = "./w4/guest.txt"
    with open(filename, "w", encoding='utf-8') as file_obj:
        file_obj.write(f"{name}") 
else:
    print("名前が入力されていません。")