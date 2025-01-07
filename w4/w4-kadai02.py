while 1:
    name = input("あなたの名前はなんですか？（終了するには「q」を入力してください）::")
    name = name.strip()

    if name == 'q': 
        break 
    if name:
        print(f"ようこそ、{name}さん！")
        filename = "./w4/guest_book.txt"
        try:
            with open(filename, "a", encoding='utf-8') as file_obj:
                file_obj.write(f"{name}\n") 
        except FileNotFoundError:
            with open(filename, "w", encoding='utf-8') as file_obj:
                file_obj.write(f"{name}\n") 
    else:
        print("名前が入力されていません。")