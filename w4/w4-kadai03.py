while 1:
    riyu = input("プログラミングが好きな理由は何ですか？（終了するには「q」を入力してください）:")
    riyu = riyu.strip()

    if riyu == 'q': 
        break 
    if riyu:
        print(f"ご入力有難うございます！")
        filename = "./w4/riyu.txt"
        try:
            with open(filename, "a", encoding='utf-8') as file_obj:
                file_obj.write(f"{riyu}\n") 
        except FileNotFoundError:
            with open(filename, "w", encoding='utf-8') as file_obj:
                file_obj.write(f"{riyu}\n") 
    else:
        print("理由が入力されていません。")