while 1:
    ninzu = input("夕食の参加人数を整数で入力してください：")
    try:
        ninzu = int(ninzu)
        break
    except ValueError:
        print("無効な入力です。整数で入力してください。")

if ninzu >= 8:
    print("テーブルが空くのを待ってください。")
else:
    print("テーブルのご用意が出来ました。")