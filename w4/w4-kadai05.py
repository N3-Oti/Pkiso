while 1:
    try:
        x = float(input("xに代入する数字を入力してください。:"))
        y = float(input("yに代入する数字を入力してください。:"))
    except ValueError:
        print("数字を入力してください。")
    else:
        kei = x + y
        print(f"x+y={x}+{y}={kei}")
        break